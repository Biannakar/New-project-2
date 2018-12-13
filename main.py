import local
while True:
  text = str(input(local.text))
  const = str(input(local.constant))
  vowel = local.vowels
  for num in range(len(vowel)):
    text = text.replace(vowel[num],vowel[num] + const + vowel[num].lower())
  print(text)
  choice = str(input(local.end))
  if choice == local.stop:
    break
  else:
    continue