require 'sequel'
require 'sqlite3'
require 'terminal-table'

class String
  def truncate(length)
    self[0..length].concat(self.length > length ? "..." : "")
  end

  def multiline(length)
    return self if self.length < length
    self[0..length-1].concat("\n#{self[length..-1].multiline(length)}")
  end
end

hwfile = ARGV[0]
dbfile = ARGV[1]

db = Sequel.sqlite(dbfile)

if !hwfile || !dbfile
  puts "you need to add the homework file and/or database file"
  exit
end

#parse empty times for q1
db.run("UPDATE races SET time = NULL WHERE time = CHAR(0)")

queries = `python3 #{hwfile}`.strip.gsub("\t", "").split("\n\n\n").map{it.gsub("\n", " ")}
queries[-1].gsub!("Your submission is valid.", "").chomp! #remove the valid submission thing

if queries.empty? || queries[0] =~ /invalid/i
  puts "your queries do not exist or there was an error :("
  exit
end

queries.each_with_index do |query, index|
  next if query =~ /Your code/i #if not written skip

  results = db.fetch(query).all
  if results.empty?
    puts "empty"
    next
  end

  headers = results[0].keys.map(&:to_s)
  rows = results.map(&:values)

  puts Terminal::Table.new(
    title: "query #{index + 1}\n#{query.multiline(100)}",
    headings: headers,
    rows: rows
  )
end