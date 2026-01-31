require 'sequel'
require 'sqlite3'
require 'terminal-table'

hwfile = ARGV[0]
dbfile = ARGV[1]

db = Sequel.sqlite(dbfile)

queries = `python3 #{hwfile}`.split("\n").map(&:strip).reject(&:empty?).tap{binding.irb}[0..-2] #removes "your submission is valid"

if queries.empty? || queries[0] =~ /invalid/i
  puts "your queries do not exist or there was an error :("
  exit
end

queries.each_with_index do |query, index|
  next if query =~ /Your code/i #if not written skip

  results = db.run(query).all
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