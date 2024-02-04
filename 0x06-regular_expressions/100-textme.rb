#!/usr/bin/env ruby
def TextMe(text)
    sender = text.match(/From: (\w+)/)&.captures&.first
    reciver = text.match(/To: (\w+)/)&.captures&.first
    flags = text.scan(/Flags: (\w+)/).flatten

    word_count = text.scan(/\b\w+\b/).count
    sentence_count = text.scan(/[^.!?]+[.!?]/).count
    character_count = text.gsub(/\s+/, '').length
    
    puts "Sender: #{sender}"
  puts "Receiver: #{receiver}"
  puts "Flags: #{flags.join(', ')}"
  puts "Word count: #{word_count}"
  puts "Sentence count: #{sentence_count}"
  puts "Character count: #{character_count}"
end