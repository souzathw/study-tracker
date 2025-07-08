/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        creme: "#fdf6e3",     
        azul: "#60A5FA",        
      },
    },
  },
  plugins: [],
}
