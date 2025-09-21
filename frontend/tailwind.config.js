/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'gemini-blue': {
          DEFAULT: '#1a73e8',
          'hover': '#1558c0',
          'focus': '#0d3c91',
          'dark': '#0d47a1',
        },
        'user-blue': {
          DEFAULT: '#4285f4',
          'dark': '#5c6bc0',
        }
      }
    },
  },
  plugins: [],
}
