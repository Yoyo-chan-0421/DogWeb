/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

// npx tailwindcss -i Dog/static/css/input.css -o ./Dog/static/output.css --watch