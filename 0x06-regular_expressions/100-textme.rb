#!/usr/bin/env ruby
from =  ARGV[0].scan(/(?<=from:).?\w+/).join
to = ARGV[0].scan(/(?<=to:).?\w+/).join
flag = ARGV[0].scan(/(?<=flags:)(.*?)\]/).join
puts "#{from},#{to},#{flag}"
