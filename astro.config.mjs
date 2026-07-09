import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://lily.smartintegrate.co.za',
  output: 'static',
  integrations: [sitemap()],
});
