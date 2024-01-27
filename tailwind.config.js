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
        
            "primary": "#F3B44B",   //#FF6B6B #3372a8  #DC7E19  #FFFAEB 
            "secondary": "#FFF5D6",
            "background": "#FFFAEB",
            "accent": "#007ACC",
            "neutral": "#FFFAEB",
            "base-100": "#F5F5F5",  //
            "info": "#4f88e3",
            "success": "#33e6b3",     
            "warning": "#f6db6f",    
            "error": "#f93e6a",
            "see": "rgba(0, 0, 0, 0.5)",
                     
        },
      },
    ],
  },
  plugins: [require("daisyui")],
}

// npx tailwindcss -i Dog/static/css/input.css -o ./Dog/static/output.css --watch
// rm -rf node_modules 
// rm package-lock.json
