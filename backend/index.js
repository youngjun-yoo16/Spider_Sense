const express = require('express')
const app = express()
const port = 3001

app.use(express.static('public'))
app.use('/css', express.static(__dirname + 'public/css'))
app.use('/js', express.static(__dirname + 'public/js'))
app.use('/img', express.static(__dirname + 'public/img'))

app.set('views', './views');
app.set('view engine', 'ejs');

app.get('', (req, res) => {
    res.sendFile(__dirname + '/views/Sentence.html')
 })

app.get('/Article.html', (req, res) => {
  res.sendFile(__dirname + '/views/Article.html')
})

app.get('/Claims.html', (req, res) => {
    res.sendFile(__dirname + '/views/Claims.html')
  })

app.get('/About.html', (req, res) => {
    res.sendFile(__dirname + '/views/About.html')
})

app.listen(port, () => console.info(`App listening on port ${port}`))

