const decode_file = (filePath) => {
  if (!filePath) {
    console.error('No file provided!')
    return
  }

  const fileText = require('fs').readFileSync(filePath, 'utf-8')
  const lines = fileText.split(/\r?\n/).map(line => {
      const [key, word] = line.split(' ')
      if (key && word) return { key: key - 1, word }
    }).filter(Boolean).sort((a, b) => a.key - b.key)

  let width = 1,
      last = 0,
      result = '';

  lines.forEach(({ key, word }) => {
    if (last === key) {
      width += 1;
      last += width;
      result += word + ' ';
    }
  })

  return result.trim()
}

const decodedMessage = decode_file('input-2.txt')
console.log(decodedMessage)
