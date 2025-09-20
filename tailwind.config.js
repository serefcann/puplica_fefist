/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'gemini-blue': '#4285f4',
        'gemini-gray': '#f8f9fa',
        'gemini-dark-gray': '#5f6368',
        'gemini-light-gray': '#e8eaed',
      },
      animation: {
        'bounce-slow': 'bounce 1.5s infinite',
        'pulse-slow': 'pulse 2s infinite',
      }
    },
  },
  plugins: [],
}

