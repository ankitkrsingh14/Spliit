/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    
    colors:{
      "Black-Olive":"#3D4543",
      "Black":"#010000",
      "Tickle-Me-Pink":"#F785AB",
      "Celeste":"#9FF9EA",
      "White":"#FDFDFD",
      "BUff":"#F6E088",
      "Celadon-blue":"#4C849F",
      transparent:'transparent',
      
    },
    extend: {},
  },
  plugins: [
    require('autoprefixer'),
  ],
}
