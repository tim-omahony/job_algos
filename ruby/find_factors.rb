def prime_factors(num)
  prime_array = []
  prime = 2
  if num < 2
    return prime
  end

  while prime < num
    prime_array << prime if num % prime == 0
    prime += 1
  end
  prime_array.join(", ")
end

puts prime_factors(1340)