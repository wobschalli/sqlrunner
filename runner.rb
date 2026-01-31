require 'sequel'
require 'sqlite3'
require 'terminal-table'

hwfile = ARGV[0]
dbfile = ARGV[1]

db = Sequel.sqlite(dbfile)

if !hwfile || !dbfile
  puts "you need to add the homework file and/or database file"
  exit
end

#parse empty times for q1
db.run("UPDATE races SET time = NULL WHERE time = CHAR(0)")

queries = `python3 #{hwfile}`.split("\n").map(&:strip).reject(&:empty?)[0..-2] #removes "your submission is valid"

if queries.empty? || queries[0] =~ /invalid/i
  puts "your queries do not exist or there was an error :("
  exit
end

queries.each_with_index do |query, index|
  next if query =~ /Your code/i #if not written skip

  puts "running query: #{query}"
  results = db.fetch(query).all
  if results.empty?
    puts "empty"
    next
  end

  headers = results[0].keys.map(&:to_s)
  rows = results.map(&:values)

  puts Terminal::Table.new(
    title: "query #{index + 1}\n#{query}",
    headings: headers,
    rows: rows
  )
end