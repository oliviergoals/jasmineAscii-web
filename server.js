const imageToAscii = require("image-to-ascii");

// The path can be either a local path or an url
// imageToAscii("./jasmine-image.jpeg", (err, converted) => {
//     console.log(err || converted);
// });

// // Passing options
imageToAscii("./jasmine-image.jpeg", {
    colored: false,
    pixels:"EDCBA "
}, (err, converted) => {
    console.log(err || converted);
});
