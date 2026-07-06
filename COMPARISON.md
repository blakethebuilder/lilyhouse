# Lily House Website — Current vs New

## Overview

| | Current | New |
|---|---|---|
| **Platform** | WordPress + Elementor | Astro 5 (static site generator) |
| **Hosting** | Bluehost (shared) | Self-hosted VPS (Dokploy) |
| **Cost** | ~R400/mo hosting + plugins | Included in existing VPS (no extra cost) |
| **Speed** | Moderate (shared hosting) | Fast (static HTML, CDN-ready) |
| **Security** | WordPress updates, plugin vulns | No database, no admin panel to attack |
| **Maintenance** | Ongoing WP updates + backups | Push to GitHub → auto-deploy |

## Pages

| Current | New | Notes |
|---------|-----|-------|
| Home | Home | ✅ Same content, faster, modern |
| About Us | About | ✅ Restructured |
| Claremont | /campuses/claremont | ✅ Dedicated page with full content, team photos, social links |
| Durbanville (nitida) | /campuses/durbanville | ✅ Same (old URL 404'd — found at /lily-house-nitida) |
| Melkbos | /campuses/melkbos | ✅ Dedicated page with full content |
| Admissions | Admissions | ✅ Fees table + enrollment form |
| Blog | Blog + 2 posts | ✅ Same posts, static |
| Contact | Contact | ✅ Campus addresses, maps, contact form |
| Our Leadership | — | ❌ Not built yet. Content exists on their site (Caitlin Brint + team). |

## Design & Features

| | Current | New |
|---|---|---|
| **Visual match** | Elementor template | Custom, matched to brand |
| **Mobile** | Responsive (Elementor) | Mobile-first, full-screen hero |
| **Animations** | None | fadeUp on hero + page sections |
| **Forms** | Elementor forms → email | Static (needs backend) |
| **Fonts** | System fonts | Raleway (Google Fonts) |
| **Colors** | Teal #00729A, Green #009A4C, White | Same — brand-matched |
| **Video tours** | None | YouTube placeholders on each campus page (add URLs when ready) |
| **Social links** | Footer per campus | Footer per campus with icons |

## What the new site enables

| Capability | How |
|------------|-----|
| **Tour booking** | Add Directus flow + WhatsApp notification |
| **Enrollment pipeline** | Connect form → CRM |
| **Parent portal** | Directus auth + private pages |
| **Per-campus analytics** | Track inquiries → tours → enrollments |
| **WhatsApp comms** | Evolution API (already running) |
| **Blog CMS** | Directus instead of WordPress |
| **Fee calculator** | Interactive widget |

## Gaps to close

| Item | Status | Action |
|------|--------|--------|
| Social URLs | Placeholder to lilyhouseschool.co.za | Already extracted from WP footer — ready to wire up. |
| Google Maps coords | Placeholder coordinates | Provide real map coords per campus |
| YouTube tour videos | Grey placeholder | Upload to YouTube, share URLs |
| Forms | Submit to # | Connect to Directus or email API |
| Our Leadership page | Not built | Content exists at /our-leadership/ — Caitlin Brint + team |
