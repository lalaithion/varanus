extern crate crypto;
extern crate byteorder;
extern crate bigint;

use std::io::prelude::*;
use std::fs::OpenOptions;
use std::fs::File;
use std::io::BufReader;

use crypto::{digest::Digest, sha2::Sha256};

use byteorder::{BigEndian, WriteBytesExt};

use bigint::{U256};

macro_rules! assert_ok(
    ($result:expr) => {
        match $result {
            Ok(..) => {},
            Err(..) => assert!(false, "got Err(..), expected Ok(..)"),
        }
    };
);

pub fn valid(bytes: &[u8; 32]) -> bool {
    let difficulty = U256::max_value() / (U256::from(100u32));

    let hashnum = U256::from(bytes.iter().as_slice());

    hashnum < difficulty
}

pub fn hash_u32(num : u32) -> [u8; 4] {
    let mut wtr = vec![];
    let mut result = [0; 4];

    wtr.write_u32::<BigEndian>(num).unwrap();
    result.clone_from_slice(&wtr);

    result
}

pub fn to_hex_string(bytes: &[u8]) -> String {
    let strs: Vec<String> = bytes
        .iter()
        .map(|b| format!("{:02X}", b))
        .collect();

    strs.join("")
}


pub fn from_hex_string(s: &str) -> [u8; 32] {
    let mut res : [u8; 32] = [0; 32];
    let mut i : usize = 0;

    for b in s.as_bytes().chunks(2) {
        let b0 = (b[0] as char).to_digit(16).unwrap() as u8;
        let b1 = (b[1] as char).to_digit(16).unwrap() as u8;
        res[i] = (b0 * 16) + b1;
        i += 1
    }

    res
}


#[derive(Debug)]
struct LogEntry {
    data: String
}


fn entry_hash(e : &LogEntry) -> [u8; 32] {
    let mut hasher = Sha256::new();
    let mut result = [0; 32];

    hasher.input(e.data.as_bytes());
    hasher.result(&mut result);

    result
}

#[derive(Debug)]
struct LogBlock {
    entry: LogEntry,
    nonce: u32,
    previous_hash: [u8; 32]
}

fn mk_log_block(msg : String, prev_hash: &[u8; 32]) -> LogBlock {
    let mut prev = [0; 32];
    prev.copy_from_slice(prev_hash);

    let entry = LogEntry{data: msg};

    let mut curr = LogBlock{entry: entry, nonce: 0, previous_hash: prev};

    while !valid(&block_hash(&curr)) {
        curr.nonce += 1;
    }

    curr
}

fn format_block(b: &LogBlock) -> String {
    let mut strs = Vec::new();
    let hash = to_hex_string(&block_hash(&b));
    let prev = to_hex_string(&b.previous_hash);
    let curr = to_hex_string(&entry_hash(&b.entry));
    let data = &b.entry.data;

    strs.push(hash);
    strs.push(":".to_string());
    strs.push(prev);
    strs.push(":".to_string());
    strs.push(format!("{:08}", b.nonce));
    strs.push(":".to_string());
    strs.push(curr);
    strs.push(":".to_string());
    strs.push(data.to_owned());

    let mut res = strs.join(" ");
    res.push('\n');
    res
}


fn block_hash(e : &LogBlock) -> [u8; 32] {
    let mut result = [0; 32];
    let subhash = entry_hash(&e.entry);

    let mut hasher = Sha256::new();
    hasher.input(&e.previous_hash);
    hasher.input(&subhash);
    hasher.input(&hash_u32(e.nonce));
    hasher.result(&mut result);

    result
}

pub trait Logger {
    fn new(init_hash: [u8; 32], location: &str) -> Self;
    fn log(&mut self, msg : &str) -> Result<(), std::io::Error>;
}

pub struct LogMemory {
    last_hash: [u8; 32],
    blocks: Vec<LogBlock>
}

impl Logger for LogMemory {
    fn new(init_hash: [u8; 32], _location: &str) -> LogMemory {
        LogMemory{last_hash: init_hash, blocks: Vec::new()}
    }

    fn log(&mut self, msg: &str) -> Result<(), std::io::Error> {
        let block = mk_log_block(msg.to_owned(), &self.last_hash);
        let hash = block_hash(&block);
        self.blocks.push(block);
        self.last_hash = hash;
        Ok(())
    }
}

pub struct LogFile {
    last_hash: [u8; 32],
    filename: String
}

impl Logger for LogFile {
    fn new(init_hash: [u8; 32], location: &str) -> LogFile {
        LogFile{last_hash: init_hash, filename: location.to_owned()}
    }

    fn log(&mut self, msg: &str) -> Result<(), std::io::Error> {
        let block = mk_log_block(msg.to_owned(), &self.last_hash);
        let hash = block_hash(&block);

        let mut file = OpenOptions::new().append(true).create(true).open(&self.filename)?;

        file.write(format_block(&block).as_bytes())?;

        self.last_hash = hash;

        Ok(())
    }
}


pub fn validate(filename: &str) -> Result<bool, std::io::Error> {
    let f = BufReader::new(File::open(filename)?);

    for line in f.lines() {
        println!("{:?}", line);
        let okline = line?;
        let mut parts = okline.split(" : ");
        let hashstr = parts.next().unwrap();
        let prevstr = parts.next().unwrap();
        let noncestr = parts.next().unwrap();
        let datahash = parts.next().unwrap();
        let data : Vec<&str> = parts.collect();
        let data = data.join(" : ");

        let block = LogBlock {
            entry: LogEntry {data : data},
            nonce: noncestr.parse::<u32>().unwrap(),
            previous_hash: from_hex_string(prevstr)
        };

        println!("{:?}", block);

        let hash = block_hash(&block);
        assert_eq!(hashstr, to_hex_string(&hash));
    }

    Ok(true)
}


#[cfg(test)]
mod tests {
    use *;

    #[test]
    fn write_log() {
        let mut logger = LogFile::new([0;32], "write_log_test.logc");
        assert_ok!(logger.log("Hello world!"));
        assert_ok!(logger.log("This is a test."));
        assert_ok!(logger.log("Alright!"));
    }

    #[test]
    fn hex_strs() {
        let arr = [1,2,3,4,5,6,7,8,
            9,10,11,12,13,14,15,16,
            17,18,19,20,21,22,23,24,
            25,26,27,28,29,30,31,32];

        assert_eq!(arr, from_hex_string(&to_hex_string(&arr)));
    }

    #[test]
    fn validate_log() {
        let mut logger = LogFile::new([0;32], "write_log_test.logc");
        assert_ok!(logger.log("Hello world!"));
        assert_ok!(logger.log("This is a test."));
        assert_ok!(logger.log("Alright!"));

        let res = validate("write_log_test.logc");
        assert_ok!(res);
        let b = res.unwrap();
        assert!(b);
    }
}
