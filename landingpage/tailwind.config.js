/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    fontFamily:{
      'lato':['lato','sans-serif'],
      'inter':['inter','sans-serif'],
      'poppins':['poppins','sans-serif']
    },
    colors:{
      transparent: 'transparent',
      "Black-Olive":"#3D4543",
      "Black":"#010000",
      "Tickle-Me-Pink":"#F785AB",
      "Celeste":"#9FF9EA",
      "White":"#FDFDFD",
      "BUff":"#F6E088",
      "Celadon-blue":"#4C849F",
    },
    extend: {},
  },
  plugins: [],
}
