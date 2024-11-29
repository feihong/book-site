{
  const links = Array.from(document.querySelectorAll('table[cellpadding="8"] tr td a'))
    .map(a => a.href)
  console.log(links.join('\n'))
}
