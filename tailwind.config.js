/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./dist/**/*.html",
    "./src/**/*.{html,js}",
  ],
  darkMode: 'media',
  theme: {
    extend: {
      fontFamily: {
        'nothingyoucoulddo': ['Nothing You Could Do', 'cursive'],
        'signika': ['Signika', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
