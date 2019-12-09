#!/usr/bin/env julia

function calculateFull(mass::Integer) ::Integer
   return trunc(mass / 3) - 2
end


function otherFuel(mass::Integer) ::Integer
   submass = calculateFull(mass)
   if submass <= 0
      return 0
   end
   return submass + otherFuel(submass)
end


open("input", "r") do masses
   fuel = map(mass -> calculateFull(parse(Int, mass)), eachline(masses))
   print(fuel, "\n")
   print(sum(fuel), "\n")
end


open("input", "r") do masses
   fuel = map(mass -> otherFuel(parse(Int, mass)), masses)
   print(fuel, "\n")
   print(sum(fuel), "\n")
end
