var markdownpdf = require("markdown-pdf")

var options = {
    highlightCssPath: 'style.css'
}

console.log("Converting ...");

markdownpdf(options).from("input.md").to("output.pdf", function () {
  console.log("Done")
})
