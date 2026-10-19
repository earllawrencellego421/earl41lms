# One Piece Theme Builder for index.html
part1 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#120c08">
<title>earl41 LMS · One Piece Grand Line Reviewer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bangers&family=Cinzel:wght@600;700;800;900&family=Pirata+One&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root {
  --straw-yellow: #f5bc25;
  --straw-gold: #e29b12;
  --luffy-red: #d32027;
  --luffy-crimson: #9e141a;
  --marine-navy: #0b1a2e;
  --grand-deep: #060e18;
  --ocean-blue: #143e64;
  --ocean-azure: #1b6899;
  --sea-foam: #e1f4fb;
  --parchment: #f9f3db;
  --parchment-mid: #eedfb8;
  --parchment-border: #c8b27d;
  --ink-black: #1b130e;
  --ink-brown: #3f2715;
  --wood-plank: #2c1a0e;
  --wood-dark: #190f08;
  --gold-accent: #fcd34d;
  --gold-bright: #ffe277;
  --white: #ffffff;
  --font-pirate: "Pirata One", cursive, serif;
  --font-hero: "Bangers", impact, sans-serif;
  --font-bounty: "Cinzel", Georgia, serif;
  --font-body: "Plus Jakarta Sans", system-ui, -apple-system, sans-serif;
  color-scheme: dark;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-body);
  color: var(--parchment);
  line-height: 1.5;
  min-height: 100vh;
  font-weight: 500;
  background-color: var(--grand-deep);
  background-image: 
    radial-gradient(ellipse 90% 60% at 50% 0%, rgba(27,104,153,0.35) 0%, rgba(11,26,46,0.85) 60%, var(--grand-deep) 100%),
    repeating-linear-gradient(45deg, rgba(255,255,255,0.015) 0 2px, transparent 2px 8px),
    linear-gradient(180deg, #091728 0%, #050d17 100%);
  background-attachment: fixed;
  padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
  position: relative;
  overflow-x: hidden;
}

:focus-visible {
  outline: 3px solid var(--straw-yellow);
  outline-offset: 3px;
}

.wrap {
  width: min(1200px, 100% - 2.5rem);
  margin-inline: auto;
}

/* TOP PIRATE GALLEY BAR */
header.bar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: 
    linear-gradient(180deg, rgba(44,26,14,0.98), rgba(25,15,8,0.98)),
    repeating-linear-gradient(90deg, transparent 0 60px, rgba(0,0,0,0.35) 60px 62px);
  border-bottom: 3px solid var(--straw-gold);
  box-shadow: 0 8px 24px rgba(0,0,0,0.65), 0 2px 0 rgba(255,255,255,0.08) inset;
  backdrop-filter: blur(8px);
}
.bar .wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-block: 0.65rem;
}
.brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
  color: var(--parchment);
  transition: transform 0.2s ease;
}
.brand:hover {
  transform: scale(1.02);
}
.brand-flag {
  width: 48px;
  height: 48px;
  background: radial-gradient(circle at 40% 40%, #201712, #0d0805);
  border: 2px solid var(--straw-yellow);
  border-radius: 50%;
  display: grid;
  place-items: center;
  box-shadow: 0 0 12px rgba(245, 188, 37, 0.4), inset 0 0 6px rgba(0,0,0,0.8);
}
.brand-flag svg {
  width: 32px;
  height: 32px;
}
.brand-title {
  display: flex;
  flex-direction: column;
}
.brand-title b {
  font-family: var(--font-pirate);
  font-size: 1.85rem;
  line-height: 1;
  letter-spacing: 0.04em;
  color: var(--parchment);
  text-shadow: 2px 2px 0 var(--ink-black), 0 0 8px rgba(245,188,37,0.3);
}
.brand-title b span {
  color: var(--straw-yellow);
}
.brand-title small {
  font-family: var(--font-bounty);
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--parchment-mid);
  opacity: 0.85;
}
.header-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(211,32,39,0.18);
  border: 1px solid rgba(211,32,39,0.5);
  padding: 0.35rem 0.85rem;
  border-radius: 999px;
  font-family: var(--font-bounty);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--gold-bright);
  letter-spacing: 0.05em;
  box-shadow: 0 0 12px rgba(211,32,39,0.25);
}
.header-badge .skull-dot {
  width: 10px;
  height: 10px;
  background: var(--luffy-red);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--luffy-red);
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.7; }

part2 = """
/* HERO SECTION */
.hero {
  position: relative;
  overflow: hidden;
  padding-block: clamp(2.5rem, 6vw, 4.5rem) clamp(3.5rem, 7vw, 5.5rem);
  text-align: center;
  border-bottom: 2px solid rgba(245, 188, 37, 0.25);
  background: 
    radial-gradient(circle at 50% 25%, rgba(27, 104, 153, 0.45) 0%, transparent 65%),
    linear-gradient(180deg, rgba(11,26,46,0.95) 0%, rgba(6,14,24,0.98) 100%);
}
.hero-particles {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}
.hero-particles i {
  position: absolute;
  bottom: -20px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(252,211,77,0.9), rgba(211,32,39,0.3));
  box-shadow: 0 0 10px rgba(252,211,77,0.8);
  animation: floatUp 8s linear infinite;
}
@keyframes floatUp {
  0% { transform: translateY(0) scale(0.6) rotate(0deg); opacity: 0; }
  20% { opacity: 0.8; }
  80% { opacity: 0.8; }
  100% { transform: translateY(-700px) scale(1.2) rotate(360deg); opacity: 0; }
}

.hero-seal {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: rgba(245, 188, 37, 0.12);
  border: 1.5px solid var(--straw-yellow);
  padding: 0.45rem 1.2rem;
  border-radius: 999px;
  font-family: var(--font-bounty);
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--straw-yellow);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 1.3rem;
  box-shadow: 0 0 16px rgba(245, 188, 37, 0.25);
}
.hero-title {
  font-family: var(--font-pirate);
  font-size: clamp(3rem, 9vw, 6.5rem);
  line-height: 0.95;
  color: var(--straw-yellow);
  text-shadow: 
    3px 3px 0 var(--luffy-crimson),
    6px 6px 0 var(--ink-black),
    0 0 25px rgba(245, 188, 37, 0.45);
  letter-spacing: 0.02em;
  margin-inline: auto;
  transform: rotate(-1deg);
}
.hero-title small {
  display: block;
  font-family: var(--font-hero);
  font-size: clamp(1.4rem, 4vw, 2.7rem);
  color: var(--white);
  letter-spacing: 0.05em;
  margin-top: 0.4rem;
  text-shadow: 
    2px 2px 0 var(--marine-navy),
    4px 4px 0 var(--ink-black),
    0 0 16px rgba(255,255,255,0.3);
  transform: rotate(1deg);
}
.hero p {
  max-width: 54ch;
  margin: 1.4rem auto 0;
  font-size: clamp(1rem, 2.2vw, 1.2rem);
  color: var(--parchment);
  font-weight: 600;
  text-shadow: 0 2px 6px rgba(0,0,0,0.7);
  line-height: 1.6;
}

/* STATS - TREASURE BOUNTIES */
.stats {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.1rem;
  margin-top: 2.2rem;
}
.stat-box {
  background: 
    linear-gradient(135deg, rgba(249,243,219,0.96), rgba(238,223,184,0.95));
  border: 3px solid var(--straw-gold);
  border-radius: 14px;
  padding: 0.75rem 1.4rem;
  box-shadow: 
    0 6px 0 var(--ink-brown),
    0 12px 20px rgba(0,0,0,0.5),
    inset 0 0 10px rgba(197, 153, 75, 0.35);
  color: var(--ink-black);
  display: flex;
  align-items: center;
  gap: 0.85rem;
  min-width: 175px;
  position: relative;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.stat-box:hover {
  transform: translateY(-3px);
  box-shadow: 
    0 9px 0 var(--ink-brown),
    0 16px 24px rgba(0,0,0,0.6);
}
.stat-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--marine-navy);
  color: var(--straw-yellow);
  display: grid;
  place-items: center;
  border: 2px solid var(--straw-gold);
  box-shadow: inset 0 0 6px rgba(0,0,0,0.7);
  flex-shrink: 0;
}
.stat-info {
  text-align: left;
}
.stat-info strong {
  font-family: var(--font-bounty);
  font-size: 1.7rem;
  font-weight: 900;
  line-height: 1;
  color: var(--luffy-crimson);
  display: block;
  letter-spacing: -0.02em;
}
.stat-info span {
  font-family: var(--font-bounty);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-brown);
}

/* WAVE SVG SEPARATOR */
.wave-divider {
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  height: 38px;
  z-index: 2;
  pointer-events: none;
}
.wave-divider path {
  fill: var(--grand-deep);
}
"""

}
"""
