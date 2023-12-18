/** @type {import('tailwindcss').Config} */
import colors from "tailwindcss/colors";
import { createThemes } from "tw-colors";

export default {
    content: [
    "./core/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "class",

  theme: {
    extend: {
      fontSize: {
        "display-large": [
          "57px",
          {
            lineHeight: "64px",
            letterSpacing: "-0.25px",
            fontWeight: "400",
          },
        ],
        "display-medium": [
          "45px",
          {
            lineHeight: "52px",
            letterSpacing: "-0.25px",
            fontWeight: "400",
          },
        ],
        "display-small": [
          "36px",
          {
            lineHeight: "44px",
            letterSpacing: "",
            fontWeight: "400",
          },
        ],
        "headline-large": [
          "32px",
          {
            lineHeight: "40px",
            letterSpacing: "",
            fontWeight: "400",
          },
        ],
        "headline-medium": [
          "28px",
          {
            lineHeight: "36px",
            letterSpacing: "",
            fontWeight: "400",
          },
        ],
        "headline-small": [
          "24px",
          {
            lineHeight: "32px",
            letterSpacing: "",
            fontWeight: "400",
          },
        ],
        "title-large": [
          "22px",
          {
            lineHeight: "28px",
            letterSpacing: "",
            fontWeight: "400",
          },
        ],
        "title-medium": [
          "16px",
          {
            lineHeight: "24px",
            letterSpacing: "0.1px",
            fontWeight: "500",
          },
        ],
        "title-small": [
          "14px",
          {
            lineHeight: "20px",
            letterSpacing: "0.1px",
            fontWeight: "500",
          },
        ],
        "label-large": [
          "14px",
          {
            lineHeight: "20px",
            letterSpacing: "0.1px",
            fontWeight: "400",
          },
        ],
        "label-medium": [
          "12px",
          {
            lineHeight: "16px",
            letterSpacing: "0.5px",
            fontWeight: "400",
          },
        ],
        "label-small": [
          "11px",
          {
            lineHeight: "16px",
            letterSpacing: "0.5px",
            fontWeight: "400",
          },
        ],
        "body-large": [
          "16px",
          {
            lineHeight: "26px",
            letterSpacing: "0.5px",
            fontWeight: "400",
          },
        ],
        "body-medium": [
          "14px",
          {
            lineHeight: "22px",
            letterSpacing: "0.25px",
            fontWeight: "400",
          },
        ],
        "body-small": [
          "12px",
          {
            lineHeight: "18px",
            letterSpacing: "0.4px",
            fontWeight: "400",
          },
        ],
        caption: [
          "12px",
          {
            lineHeight: "16px",
            letterSpacing: "0.4px",
            fontWeight: "400",
          },
        ],
        overline: [
          "12px",
          {
            lineHeight: "16px",
            letterSpacing: "0.5px",
            fontWeight: "500",
          },
        ],
      },

      borderRadius: {
        "extra-small": "4px",
        small: "8px",
        medium: "12px",
        large: "16px",
        "extra-large": "28px",
      },

      boxShadow: {
        "mm-1":
          "0px 1px 2px 0px rgba(0, 0, 0, 0.05), 0px 1px 3px 1px rgba(0, 0, 0, 0.10)",
        "mm-2":
          "0px 1px 2px 0px rgba(0, 0, 0, 0.15), 0px 2px 6px 2px rgba(0, 0, 0, 0.15)",
        "mm-3":
          "0px 4px 8px 3px rgba(0, 0, 0, 0.15), 0px 1px 3px 0px rgba(0, 0, 0, 0.3)",
        "mm-4":
          "0px 6px 10px 4px rgba(0, 0, 0, 0.15), 0px 2px 3px 0px rgba(0, 0, 0, 0.3)",
        "mm-5":
          "0px 8px 12px 6px rgba(0, 0, 0, 0.15), 0px 4px 4px 0px rgba(0, 0, 0, 0.3)",
      },

      animation: {
        "blob-short": "blob-short 15s linear infinite",
        "fade-in": "fade-in 0.2s cubic-bezier(0.2, 0.0, 0, 1.0) 1",
        "gradient-x": "gradient-x 15s ease infinite",
        "gradient-xy": "gradient-xy 15s ease infinite",
        "gradient-y": "gradient-y 15s ease infinite",
        "sliding-img-down-1": "sliding-img-down-1 30s linear infinite",
        "sliding-img-up-1": "sliding-img-up-1 45s linear infinite",
        "sliding-img-up-2": "sliding-img-up-2 60s linear infinite",
        "spin-lazy": "spin-lazy 5s linear infinite",
        "transition-bottom":
          "transition-bottom 0.4s cubic-bezier(0.2, 0.0, 0, 1.0) 1",
        "transition-left":
          "transition-left 0.4s cubic-bezier(0.2, 0.0, 0, 1.0) 1",
        "transition-right":
          "transition-right 0.4s cubic-bezier(0.2, 0.0, 0, 1.0) 1",
        "transition-top":
          "transition-top 0.2s cubic-bezier(0.2, 0.0, 0, 1.0) 1",
        "transition-top-lazy":
          "transition-top 4s cubic-bezier(0.2, 0.0, 0, 1.0) 1",
        blob: "blob 25s cubic-bezier(0.2, 0.0, 0, 1.0) infinite",
        determinate: "determinate 4s cubic-bezier(.9,0,.2,1) infinite",
        indeterminate: "indeterminate 2s cubic-bezier(.7,.1,.5,1) infinite",
        moving: "moving 25s cubic-bezier(0.2, 0.0, 0, 1.0) infinite",
      },

      keyframes: {
        determinate: {
          from: {
            transform: "translateX(-100%)",
          },
          to: {
            transform: "translateX(0)",
          },
        },
        indeterminate: {
          from: {
            transform: "translateX(-100%)",
          },
          to: {
            transform: "translateX(100%)",
          },
        },
        "transition-left": {
          from: {
            transform: "translateX(-80%)",
          },
          to: {
            transform: "translateX(0)",
          },
        },
        "transition-right": {
          from: {
            transform: "translateX(80%)",
          },
          to: {
            transform: "translateX(0%)",
          },
        },
        "transition-bottom": {
          from: {
            transform: "translateY(100%)",
          },
          to: {
            transform: "translateY(0)",
          },
        },
        "transition-top": {
          from: {
            transform: "translateY(-12px)",
          },
          to: {
            transform: "translateY(0)",
          },
        },
        "fade-in": {
          from: {
            opacity: "0",
          },
          to: {
            opacity: "100",
          },
        },
        "gradient-y": {
          "0%, 100%": {
            backgroundSize: "400% 400%",
            backgroundPosition: "center top",
          },
          "50%": {
            backgroundSize: "200% 200%",
            backgroundPosition: "center center",
          },
        },
        "gradient-x": {
          "0%, 100%": {
            backgroundSize: "200% 200%",
            backgroundPosition: "left center",
          },
          "50%": {
            backgroundSize: "200% 200%",
            backgroundPosition: "right center",
          },
        },
        "gradient-xy": {
          "0%, 100%": {
            backgroundSize: "400% 400%",
            backgroundPosition: "left center",
          },
          "50%": {
            backgroundSize: "200% 200%",
            backgroundPosition: "right center",
          },
        },
        "spin-lazy": {
          "0%": {transform: "rotate(0deg)"},
          "100%": {transform: "rotate(360deg)"},
        },
        blob: {
          "0%": {
            transform: "translateX(0%) translateY(0%)",
          },
          "20%": {
            transform: "translateX(-50%) translateY(-100%)",
          },
          "40%": {
            transform: "translateX(-100%) translateY(-50%)",
          },
          "60%": {
            transform: "translateX(-50%) translateY(-0%) ",
          },
          "80%": {
            transform: "translateX(0%) translateY(-50%)",
          },
          "100%": {
            transform: "translateX(0%) translateY(0%)",
          },
        },
        "blob-short": {
          "0%": {
            transform: "translateX(0%) translateY(-30%)",
          },
          "30%": {
            transform: "translateX(-15%) rotate(-5deg) translateY(0%)",
          },
          "60%": {
            transform: "translateX(0%) rotate(5deg) translateY(30%) ",
          },
          "80%": {
            transform: "translateX(15%) rotate(-5deg) translateY(0%) ",
          },
          "100%": {
            transform: "translateX(0%) translateY(-30%)",
          },
        },
        moving: {
          "0%": {
            transform: "translateX(0%) translateY(0%)",
          },
          "20%": {
            transform: "translateX(50%) translateY(100%)",
          },
          "40%": {
            transform: "translateX(100%) translateY(50%)",
          },
          "60%": {
            transform: "translateX(50%) translateY(0%) ",
          },
          "80%": {
            transform: "translateX(0%) translateY(50%)",
          },
          "100%": {
            transform: "translateX(0%) translateY(0%)",
          },
        },

        "sliding-img-up-1": {
          "0%, 100%": {
            transform: "translateY(-50%)",
          },
          "50%": {
            transform: "translateY(-100%)",
          },
        },
        "sliding-img-up-2": {
          "0%, 100%": {
            transform: "translateY(-50%)",
          },
          "50%": {
            transform: "translateY(-100%)",
          },
        },
        "sliding-img-down-1": {
          "0%, 100%": {
            transform: "translateY(-10%)",
          },
          "50%": {
            transform: "translateY(-170%)",
          },
        },
      },
    },
  },
  plugins: [
    require("tailwind-scrollbar-hide"),
    require("@tailwindcss/forms"),
    createThemes({
      light: {
        // primary
        primary: colors.indigo[700],
        "primary-hover": colors.indigo[800],
        "inverse-primary": colors.orange[800],
        "on-primary": colors.white,
        "primary-container": colors.indigo[900],
        "on-primary-container": colors.indigo[200],
        // secondary
        secondary: colors.indigo[100],
        "secondary-hover": colors.indigo[300] + 80,
        "on-secondary": colors.indigo[800],
        "secondary-container": colors.indigo[500],
        "secondary-container-hover": colors.orange[100],
        "on-secondary-container": colors.orange[800],
        // tertiary
        tertiary: colors.indigo[300] + 20,
        "tertiary-hover": colors.lime[300] + 24,
        "on-tertiary": colors.indigo[900],
        "tertiary-container": colors.indigo[800],
        "tertiary-container-hover": colors.orange[100],
        "on-tertiary-container": colors.orange[800],
        // error
        error: colors.red[700],
        "on-error": colors.white,
        "error-container": colors.red[800],
        "on-error-container": colors.red[200],
        // surface
        "surface-container-lowest": colors.slate[300],
        "surface-container-low": colors.slate[200],
        surface: colors.white,
        "on-surface": colors.black,
        "on-surface-variant": colors.slate[600],
        "inverse-surface": colors.slate[900],
        "inverse-on-surface": colors.slate[200],
        "surface-tint": colors.indigo[800],
        "surface-container": colors.slate[100],
        "surface-container-high": colors.slate[200],
        "surface-container-highest": colors.slate[300],
        // alternative surface
        "surface-dim": colors.indigo[100],
        "surface-bright": colors.indigo[900],
        // outline
        outline: colors.slate[200],
        "outline-variant": colors.slate[300],
        // scrim
        scrim: colors.slate[900] + 30,
      },

      dark: {
        // primary
        primary: colors.violet[300],
        "primary-hover": colors.violet[400],
        "inverse-primary": colors.violet[400],
        "on-primary": colors.violet[900],
        "primary-container": colors.violet[800],
        "on-primary-container": colors.violet[200],

        // secondary
        secondary: colors.violet[300] + 20,
        "secondary-hover": colors.violet[400] + 24,
        "on-secondary": colors.violet[300],
        "secondary-container": colors.violet[400],
        "secondary-container-hover": colors.violet[900],
        "on-secondary-container": colors.violet[200],

        // tertiary
        tertiary: colors.violet[900],
        "tertiary-hover": colors.violet[800],
        "on-tertiary": colors.violet[300],
        "tertiary-container": colors.violet[300],
        "tertiary-container-hover": colors.violet[900],
        "on-tertiary-container": colors.violet[200],

        // error
        error: colors.red[400],
        "on-error": colors.red[950],
        "error-container": colors.red[800],
        "on-error-container": colors.red[200],

        // surface = background
        "surface-container-lowest": colors.zinc[700],
        "surface-container-low": colors.zinc[800],
        surface: colors.zinc[950],
        "on-surface": colors.white,
        "on-surface-variant": colors.zinc[600],
        "inverse-surface": colors.zinc[50],
        "inverse-on-surface": colors.zinc[800],
        "surface-tint": colors.violet[300],
        "surface-container": colors.zinc[900],
        "surface-container-high": colors.zinc[800],
        "surface-container-highest": colors.zinc[700],

        // alternative surface
        "surface-dim": colors.violet[900],
        "surface-bright": colors.violet[900],

        // outline
        outline: colors.zinc[800],
        "outline-variant": colors.zinc[900],

        // scrim
        scrim: colors.zinc[950] + 90,
      },
      slate: {
        // primary
        primary: colors.indigo[300],
        "primary-hover": colors.indigo[400],
        "on-primary": colors.indigo[900],
        "primary-container": colors.indigo[800],
        "on-primary-container": colors.indigo[200],

        // secondary
        secondary: colors.indigo[300] + 20,
        "secondary-hover": colors.indigo[400] + 30,
        "on-secondary": colors.indigo[300],
        "secondary-container": colors.indigo[400],
        "secondary-container-hover": colors.indigo[900],
        "on-secondary-container": colors.indigo[200],

        // tertiary
        tertiary: colors.indigo[900],
        "tertiary-hover": colors.indigo[800],
        "on-tertiary": colors.indigo[300],
        "tertiary-container": colors.indigo[300],
        "tertiary-container-hover": colors.indigo[900],
        "on-tertiary-container": colors.indigo[200],

        // error
        error: colors.red[400],
        "on-error": colors.red[950],
        "error-container": colors.red[800],
        "on-error-container": colors.red[200],

        // surface = background
        "surface-container-lowest": colors.slate[700],
        "surface-container-low": colors.slate[800],
        surface: colors.slate[950],
        "surface-container": colors.slate[900],
        "surface-container-high": colors.slate[800],
        "surface-container-highest": colors.slate[700],

        "on-surface": colors.white,
        "on-surface-variant": colors.slate[600],

        // alternative surface
        "surface-dim": colors.indigo[900],
        "surface-bright": colors.indigo[900],

        // outline
        outline: colors.slate[800],
        "outline-variant": colors.indigo[400],

        // scrim
        scrim: colors.slate[950] + 90,
      },
      neutral: {
        // primary
        primary: colors.sky[300],
        "primary-hover": colors.sky[400],
        "inverse-primary": colors.sky[400],
        "on-primary": colors.sky[900],
        "primary-container": colors.sky[800],
        "on-primary-container": colors.sky[200],

        // secondary
        secondary: colors.sky[300] + 20,
        "secondary-hover": colors.sky[400] + 24,
        "on-secondary": colors.sky[300],
        "secondary-container": colors.sky[400],
        "secondary-container-hover": colors.sky[900],
        "on-secondary-container": colors.sky[200],

        // tertiary
        tertiary: colors.sky[900],
        "tertiary-hover": colors.sky[800],
        "on-tertiary": colors.sky[300],
        "tertiary-container": colors.sky[300],
        "tertiary-container-hover": colors.sky[900],
        "on-tertiary-container": colors.sky[200],

        // error
        error: colors.red[400],
        "on-error": colors.red[950],
        "error-container": colors.red[800],
        "on-error-container": colors.red[200],

        // surface = background
        "surface-container-lowest": colors.neutral[700],
        "surface-container-low": colors.neutral[800],
        surface: colors.neutral[950],
        "on-surface": colors.white,
        "on-surface-variant": colors.neutral[600],
        "inverse-surface": colors.neutral[50],
        "inverse-on-surface": colors.neutral[800],
        "surface-tint": colors.sky[300],
        "surface-container": colors.neutral[900],
        "surface-container-high": colors.neutral[800],
        "surface-container-highest": colors.neutral[700],

        // alternative surface
        "surface-dim": colors.sky[900],
        "surface-bright": colors.sky[900],

        // outline
        outline: colors.neutral[800],
        "outline-variant": colors.neutral[900],

        // scrim
        scrim: colors.neutral[950] + 90,
      },
    }),
  ],
}

