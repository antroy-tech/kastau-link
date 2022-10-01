/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/src/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
          poppins: 'Poppins',
      }
    }
  },
  darkMode: 'class',

  plugins: [],
}