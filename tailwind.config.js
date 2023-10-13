/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/templates/**/*.html"],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: [
      {
        mytheme: {
        
            "primary": "#DC7E19",   //#FF6B6B
            "secondary": "#4CAF50",
            "accent": "#007ACC",
            "neutral": "#1f2428",
            "base-100": "#F5F5F5",  //
            "info": "#4f88e3",
            "success": "#33e6b3",     
            "warning": "#f6db6f",    
            "error": "#f93e6a",
                     
        },
      },
    ],
  },
  plugins: [require("daisyui")],
}

// npx tailwindcss -i Dog/static/css/input.css -o ./Dog/static/output.css --watch
// rm -rf node_modules 
// rm package-lock.json