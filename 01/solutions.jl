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


open("input", "r") do f
   fuel = 0
   for mass in eachline(f)
      mass = parse(Int, mass)
      fuel += calculateFull(mass)
   end
   print(fuel, "\n")
end


open("input", "r") do f
   fuel = 0
   for mass in eachline(f)
      mass = parse(Int, mass)
      fuel += otherFuel(mass)
   end
   print(fuel, "\n")
end
