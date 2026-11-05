---
title: "Changelog"
description: "Verified source changes, product updates, and deployment notes across Chaotic Minds Collective projects, including The Grease Dojo."
layout: "page"
---
# Changelog

## November 5, 2026
  ### Chaotic Solutions

  - **Repository moved to the organization**: the site repo now lives at Chaotic-Minds-Collective/chaotic-solutions-site (transferred from psyryn82), completing the GitHub migration for this site.
  - **Cloudflare migration prep**: static export was enabled for Cloudflare Pages (`output: export` with unoptimized images, [PR #4](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/4)), and a wrangler static-assets config was added for the Cloudflare deploy ([PR #5](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/5)).
  - **Vercel deployment failing**: Vercel reported on the evening of November 4 that Hobby plan deployments cannot build from private organization repositories. This is expected fallout of the org migration, not a code failure; the move to Cloudflare Pages resolves it. No live Cloudflare deployment verified yet.

  ### Collective HQ automation

  - **Automation fixes round 2 merged**: review findings on the org workflow automator were fixed (workflow permissions scoping, monitor report hardening, onboarding edge cases) and the registry entry was corrected to the new Solutions repo name ([PR #2](https://github.com/Chaotic-Minds-Collective/.github/pull/2), merged the evening of November 4). The org workflow system is fully live.

  > This entry records merged source changes. No Cloudflare Pages or Render deployment was verified at publish time.

## November 4, 2026
  ### Collective HQ handbook

  - **Handbook migration, Phase 2**: the handbook left Mintlify and became a plain-markdown GitHub Pages site. All 11 MDX sources were converted to markdown with content text unchanged, the Mintlify configuration was removed, and a Jekyll minima dark theme was added ([PR #7](https://github.com/Chaotic-Minds-Collective/docs/pull/7)).
  - **Brand styling**: electric-turquoise accents were layered over the minima dark skin ([PR #8](https://github.com/Chaotic-Minds-Collective/docs/pull/8)), then replaced with a real site-level stylesheet, a /docs baseurl, and relative content links so navigation URLs resolve on the project site ([PR #9](https://github.com/Chaotic-Minds-Collective/docs/pull/9)).
  - **Live and verified**: the handbook serves at https://chaotic-minds-collective.github.io/docs/ and was verified loading on the evening of November 4. Phase 3 (disconnecting the Mintlify app) is pending owner approval.

  ### Chaotic Command

  - **Discord OAuth fixed**: server-side Discord API calls now send a User-Agent header, resolving the Cloudflare 1015 block on the token exchange ([PR #27](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/27)). Failure-body logging for diagnosis landed first ([PR #26](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/26)).
  - **Discord bot gateway docs**: a gateway guide and docs index were added as Phase 1 of the docs migration ([PR #25](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/25)).

  ### Chaotic Gaming

  - **CI build fix**: the default Node-with-Webpack workflow was replaced with `npm run build` for the Next.js app, ending the failing check that ran on every commit ([PR #5](https://github.com/Chaotic-Minds-Collective/Chaotic-Gaming/pull/5)).
  - **README expansion**: site routes, key data files, brand-asset caveats, and deployment notes were documented as Phase 1 of the docs migration ([PR #4](https://github.com/Chaotic-Minds-Collective/Chaotic-Gaming/pull/4)). CodeQL, PR labeler, issue summarizer, and stale-issue workflows were added.

  ### The Grease Dojo

  - **Accent cleanup**: hardcoded teal accents in the ported Case Worksheet, Reference Desk, and Site Notices stylesheets were recolored to the approved fire orange, hex swaps only ([PR #26](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/26)).

  ### Chaotic Solutions

  - **Standalone inquiry page**: a full-page Tally project inquiry embed now lives at /inquiry, with a least-privilege iframe sandbox ([PR #1](https://github.com/psyryn82/chaotic-solutions-site/pull/1)).
  - **Form height fix**: Tally dynamic height was disabled so the form scrolls inside a fixed frame ([PR #3](https://github.com/psyryn82/chaotic-solutions-site/pull/3)).

  ### Chaotic Command (earlier today)

  - **Brand launch**: the homepage was rebuilt with tabbed sections, brand imagery, and real metadata, and the command center was restyled with the brand palette and sticky section tabs ([PR #23](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/23)).
  - **Mobile polish**: fixed an invisible quiet button, made the tab row scrollable, and compacted the phone layout ([PR #24](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/24)).

  ### The Grease Dojo (earlier today)

  - **Case Worksheet, Reference Desk, and Site Notices ported to main**: three unmerged components from the October 30 worksheet branch now live on main - a local-only diagnostic case-notes worksheet with copy and print, curated external references, and draft educational-use, safety, and data-handling notices ([PR #25](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/25)).
  - **Docs salvage**: six project documents (legal-review checklist, roadmap, decision log, asset inventory, reference sources, changelog) were preserved from the worksheet branch ([PR #24](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/24)).

  > This entry records merged source changes. The handbook's GitHub Pages site was verified live on the evening of November 4. The Grease Dojo's Pages deploy, Chaotic Command's Render deploy, and the Chaotic Solutions site's deploy were still not verified at publish time.

## November 3, 2026
  ### The Grease Dojo (formerly The Diagnostic Bay)

  - **Official brand name**: the venture formerly known as The Diagnostic Bay is now officially **The Grease Dojo**. Spelling confirmed by the owner on November 3, 2026.
  - The mascot and visual identity are unchanged: Don Calavera, with the Colombian-inspired palette.
  - The GitHub repository keeps its `the-diagnostic-bay` name; all new branding, copy, and public-facing pages use The Grease Dojo going forward.

  ### The Grease Dojo footer branding

  - **Approved footer tagline**: the footer now uses "WE HELP YOU FIND THE FAULT - OR TEACH YOU TO FIND IT", matching the approved header wording.
  - The source change merged in [PR #21](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/21) on November 3, 2026.

  ### Collective HQ corporate site

  - **Real artwork live**: placeholder SVGs were replaced with optimized PNG artwork, resolving the broken-image issue. Image paths were verified loading correctly on chaoticmindscollective.com on November 3. Source changes merged in [PR #3](https://github.com/Chaotic-Minds-Collective/chaotic-minds-collective/pull/3).
  - **Contact form**: a free-tier Web3Forms contact form was added and then hotfixed with the real access key ([PR #4](https://github.com/Chaotic-Minds-Collective/chaotic-minds-collective/pull/4), [PR #5](https://github.com/Chaotic-Minds-Collective/chaotic-minds-collective/pull/5)).
  - **Accessibility pass**: skip link, main landmark, navigation ARIA labels, and visible focus states were applied across all pages ([PR #6](https://github.com/Chaotic-Minds-Collective/chaotic-minds-collective/pull/6)).

  ### Chaotic Command

  - **Discord bot Milestones 1 and 2**: a Discord Gateway background worker landed with structured logging, RESUME handling, a health endpoint, graceful exit, and documented web-versus-bot environment variables. Regression tests were added through CodeRabbit review ([PR #18](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/18)).
  - **Render build fix**: the stale pnpm lockfile was regenerated and pnpm settings were pinned through .npmrc ([PR #20](https://github.com/Chaotic-Minds-Collective/Chaotic-Command/pull/20)).

  ### The Grease Dojo contact page

  - **Live contact form**: a new `#/contact` page now embeds the live "Contact Grease Dojo" Tally form, including fragment-scroll fixes ([PR #23](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/23)).
  - **Auto-deploy**: GitHub Pages now deploys automatically on every push to main ([PR #22](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/22)).

  > This entry records merged source changes, not verified live deployments. Image loading on chaoticmindscollective.com was verified on November 3; Vercel, GitHub Pages, and Render deployment statuses for Chaotic Gaming, The Grease Dojo, and Chaotic Command still need to be checked on their dashboards.

## November 2, 2026
  ### Collective HQ, Chaotic Gaming, and payments

  ### New features

  - **Chaotic Minds Collective corporate site**: the parent-organization website was built and published on GitHub Pages, with per-division badges across all pages.
  - **Public handbook publishing pending**: the handbook changelog is not yet confirmed as live. The [Mintlify documentation URL](https://chaotic-minds-collective.mintlify.app/changelog) must be checked in the rendered Mintlify preview before it is advertised as the public handbook.

  ### Updates

  - **Chaotic Gaming production deploy confirmed green on `Vercel`** - the design-v2 rebuild is live at www.chaoticmindsgaming.com, followed by an honesty pass and a branded 404 page.
  - **Chaotic Command billing**: a first recurring price was created in Stripe test mode; test-mode checkout and webhook setup continues.
  - **`Supabase`**: both free projects (Chaotic-Solutions and Chaotic-Gaming) have auto-paused. Pause is recoverable for 90 days.

  > Publishing check on November 3, 2026: the handbook changelog is reachable at https://chaotic-minds-collective.mintlify.app/changelog. The deployment record still advertises https://chaoticmindscollective.com, which currently serves the corporate website. The custom-domain mapping needs review; use the verified Mintlify URL to reach the handbook.

## November 1, 2026
  ### Chaotic Gaming, Chaotic Solutions, and The Grease Dojo

  ### New features

  - **Chaotic Gaming design system v2**: every page of the gaming division site was rebuilt on a gothic-futuristic theme with new fonts, atmosphere, and motion. A mobile hamburger menu was added for small screens.
  - **Brand badge**: nav logo, favicon, footer crest, and About crest now use the Chaotic Gaming brand assets.
  - **Live Discord invite**: all join buttons across the site point to the real server invite.

  ### Updates

  - **Chaotic Solutions site early launch**: landing page with services and pricing, a portfolio section, and a live Tally contact form wired into the contact section.
  - Added the Chaotic Solutions brand SVG mark and favicon.
  - **Payments**: Stripe business account and Treasury are set up, so Chaotic Minds Collective can now receive funds.

  ### The Grease Dojo brand assets

  - Replaced the generic brand mark with the approved skull badge used by the header, favicon reference, and info sections.
  - Updated the header to "WE HELP YOU FIND THE FAULT - OR TEACH YOU TO FIND IT" and clarified that diagnostic drafts remain under mechanic review.
  - These source changes merged in [PR #19](https://github.com/Chaotic-Minds-Collective/the-diagnostic-bay/pull/19) on November 1, 2026. This is not confirmation of a live-site relaunch.

  > Deployment status for the Chaotic Gaming site should be verified on the `Vercel` dashboard after the latest build trigger.

## October 30, 2026
  ### The Grease Dojo

  The Grease Dojo (then working under the project name "The Diagnostic Bay") is a new educational resource for automotive diagnosis and repair.

  ### New features

  - **Guided Intake**: Pick the main vehicle concern, such as no-start, rough running, a warning light, overheating, or a new noise, smell, or leak. Each path gives you an observation checklist, warning signs that mean you should stop and get help, and a safe next step.
  - **Diagnostic Lab**: Browse 12 draft OBD-II trouble-code entries. You can filter them by Engine, Air & Fuel, Electrical, and Temperature.
  - **Live search**: Search trouble codes and field guides as you type, or use the quick search options.
  - **Fix Database**: Open six interactive field guides.
  - **Symptom cards**: Select a common symptom to start a matching search.
  - **Learning Paths, safety rules, and Rules of the Bay**: Preview upcoming learning content and review the safety rules that apply across the site.

  ### Updates

  - Redesigned the homepage with a dark industrial look and an illustrative diagnostic console. The console isn't connected to a vehicle.
  - Improved accessibility with a skip link, visible keyboard focus, reduced-motion support, an accessible detail dialog, and larger touch targets.
  - Added a responsive sticky header and a mobile navigation menu.

  ### Bug fixes

  - Fixed search results opening the wrong diagnostic detail.
  - Fixed the logo and favicon not loading on the hosted site.
  - Fixed the Guided Intake link missing from the navigation on the hosted site.

  > All diagnostic content is educational and still in draft. A trouble code is evidence, not proof that a part has failed. Always follow vehicle-specific service information.
