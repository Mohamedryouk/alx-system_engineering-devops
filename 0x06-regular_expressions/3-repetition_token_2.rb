#!/usr/bin/env ruby

def matchinput(input)
    regex = /hbt+n/

    matchresult = input.match(regex)

    puts matchresult ? matchresult[0] : ''
end