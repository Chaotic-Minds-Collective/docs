---
title: "Changelog"
description: "Verified source changes, product updates, and deployment notes across Chaotic Minds Collective projects, including The Grease Dojo."
layout: "page"
---
# Changelog

## November 6, 2026
  ### Chaotic Solutions

  - **Own inquiry form replaced the Tally embed**: /contact now renders a brand-styled InquiryForm (name, email, service, budget, message) that submits directly to the Supabase inquiries table using the publishable key, protected by an insert-only RLS policy with field limits and email validation, plus a honeypot bot trap and per-field accessible inline validation. The Tally iframe was removed ([PR #13](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/13)).
  - **Gothic font root-cause fix**: headings had silently rendered in Inter because the --font-gothic theme indirection resolved empty at computed time; h1/h2 and a .font-gothic class now reference var(--font-pirata) directly with weight 400. A "Who we are" section (owner-operated, Enumclaw WA + remote) and an honest "Sites we've built" portfolio (FQ SNRG MMA, The Grease Dojo, Chaotic Command) were added ([PR #14](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/14)).
  - **Typography polish**: cyan-glow headings and brighter body text ([PR #12](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/12)).

  ### Chaotic Command

  - **Shared Discord bot on Cloudflare Workers**: the shared Chaotic Command bot landed as a serverless Worker application, including ticketing (channel and record cleanup on failure), modal parsing, and slash-command registration ([PR #45](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/45)).
  - **Deploy automation**: a manual one-shot GitHub Actions workflow deploys the bot with wrangler@4, pushes the six Worker secrets from repository secrets, registers slash commands, and prints the workers.dev URL - with secret validation, HTTPS enforcement on the Supabase URL, and redirect rejection added in review ([PR #47](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/47)).
  - **Sign-in and gateway hardening**: silent token refresh now routes through the Supabase relay ([PR #44](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/44)), and Gateway heartbeat watchdog and reconnect/quota races were fixed ([PR #46](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/46)).

  ### Chaotic Gaming

  - **Security headers**: nosniff, frame-deny with CSP frame-ancestors, strict referrer policy, disabled camera/mic/geo/payment, and a CSP allowing Vercel Analytics and Google Fonts - closing the P1 audit gap ([PR #15](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/15)).
  - **SEO basics**: robots.txt, sitemap.xml for all six public routes, and a favicon route closing the P2 audit gaps ([PR #16](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/16)).
  - **Live Discord widget**: the /discord page embeds the official server widget (online count + join) in a branded card, with CSP frame-src and responsive iframe sizing from review ([PR #17](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/17)).
  - **Platform upgrades**: adopted the org shared CI and removed superseded workflows ([PR #11](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/11)), added Vercel Web Analytics ([PR #12](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/12)), and Dependabot bumps for postcss 8.5.23 and Next.js 16.4.5 ([PR #13](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/13), [PR #14](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/14)).

  ### The Grease Dojo

  - **Security remediation merged - application still pending**: the least-privilege migration and rollback plan merged on the evening of November 5 ([PR #27](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/27)). Applying it to the Supabase project remains a separate, explicitly approved step and has not been run.
  - **Multi-page rebrand**: the site gained a multi-page layout under The Greasy Dojo identity ([PR #31](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/31)), and unused template workflows were removed ([PR #32](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/32)).
  - **Search and content**: fixed a broken hero image and made search understand natural-language questions ([PR #33](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/33)); draft transmission entries (P0700, P0715, P0730 and a conservative won't-shift guide, all mechanic-review-pending) were added and wired into search, the detail dialog, Diagnostic Lab, and the Fix Database ([PR #34](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/34)).
  - **Artwork palette**: recolored to the hero artwork's electric blue on navy-black, demoting fire orange to small highlights while keeping the Colombian tricolor accents and hero image ([PR #35](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/35)); README refreshed to the current project state, including honest draft status and verified content counts ([PR #36](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/36)).

  ### Collective HQ automation

  - **Daily monitor fixed**: the monitor now scans per-repo because the org-level endpoint 404s with fine-grained PATs, includes unlisted onboarded repos and the .github hub, reports skipped scans, and propagates errors ([PR #10](https://github.com/Chaotic-Minds-Collective/.github/pull/10)), and diagnoses Discord webhook failures in the report with verified mocked behavior ([PR #11](https://github.com/Chaotic-Minds-Collective/.github/pull/11)).
  - **Instant CI alerts**: shared-ci now calls the notify-failure workflow on push-event CI failures, so onboarded repos get Discord alerts immediately instead of up to 24h later via the daily monitor ([PR #12](https://github.com/Chaotic-Minds-Collective/.github/pull/12)).

  > Deployment verification, November 6 evening: not re-verified at publish time. A Vercel preview deployment for chaotic-gaming failed at 3:25 PM PST. Tally is no longer the Solutions intake path; the new own-form pipeline has not been tested end to end - the only row in inquiries is the November 5 synthetic Edge Function test. Customer inquiries remain at zero since launch.

## November 5, 2026
  ### Chaotic Solutions

  - **Repository moved to the organization**: the site repo now lives at Chaotic-Minds-Collective/chaotic-solutions-site (transferred from psyryn82), completing the GitHub migration for this site.
  - **Cloudflare migration prep**: static export was enabled for Cloudflare Pages (`output: export` with unoptimized images, [PR #4](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/4)), and a wrangler static-assets config was added for the Cloudflare deploy ([PR #5](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/5)).
  - **Vercel deployment failing**: Vercel reported on the evening of November 4 that Hobby plan deployments cannot build from private organization repositories. This is expected fallout of the org migration, not a code failure; the move to Cloudflare resolves it.

  ### Collective HQ automation

  - **Automation fixes round 2 merged**: review findings on the org workflow automator were fixed (workflow permissions scoping, monitor report hardening, onboarding edge cases) and the registry entry was corrected to the new Solutions repo name ([PR #2](https://github.com/Chaotic-Minds-Collective/.github/pull/2), merged the evening of November 4). The org workflow system is fully live.

  ### Chaotic Solutions (evening)

  - **Shared org CI onboarded**: the shared org CI workflow plus a trusted failure-notification workflow were added to the repo ([PR #6](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/6)).
  - **Brand assets**: favicon set, badge/emblem/icon assets, hero and OG banners, and metadata wiring ([PR #7](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/7)).
  - **Docs refresh**: README, decision log, and contact-form docs updated for the Cloudflare Workers + Supabase inquiry pipeline ([PR #8](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/8)).
  - **Mobile hero fix**: killed the blank hero void on phones, swapped the wrong Greasy Dojo logo for the approved Solutions emblem, and referenced the hero banner that had never been used ([PR #9](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/9)).
  - **Wrangler fix**: an empty previews block unblocked wrangler 4.158 preview deploys ([PR #10](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/10)).
  - **Multi-page redesign**: palette sampled from the official banner art (electric blue #2e7dff, cyan spark #18f0f0, deep navy panels), split into Home / Pricing / Contact pages with sticky nav, gothic Pirata One headings, and the Tally form on /contact ([PR #11](https://github.com/Chaotic-Minds-Collective/chaotic-solutions-site/pull/11)).
  - **Live on Cloudflare**: the chaotic-solutions-site Worker was updated right after the redesign merge and is deployed.

  ### Chaotic Command (evening)

  - **Brand assets and share previews**: favicon, brand icons, and og-image assets were added, and the OG image is now served through a public static route ([PR #30](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/30), [PR #31](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/31), [PR #33](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/33)).
  - **Database layer recovered**: the dual-driver db layer lost from main was restored, with atomic serialized migrations, remote PostgreSQL TLS verification, runtime dependencies in CI, and adapter/migration documentation ([PR #32](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/32)).
  - **Palette match and footer stamp**: the site palette was matched to the brand art (neon green with subtle purple accents) and a ring-badge stamp was added to the footer ([PR #34](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/34), [PR #35](https://github.com/Chaotic-Minds-Collective/chaotic-command/pull/35)).
  - **Render deploy verified live**: the latest deploy (footer stamp) finished at 7:31 PM PST on November 5 and is serving.

  ### Chaotic Gaming (evening)

  - **Glitch brand assets**: badge, banner, lockup, and icon assets were added under public/ ([PR #8](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/8)).
  - **CI workflow rename**: webpack.yml became node-build.yml to match the Next.js build ([PR #9](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/9)).
  - **Social share previews**: openGraph and twitter metadata now use the Glitch banner ([PR #10](https://github.com/Chaotic-Minds-Collective/chaotic-gaming/pull/10)).
  - **Render deploy verified live**: the latest deploy (share previews) finished at 5:54 PM PST on November 5 and is serving.

  ### The Grease Dojo (evening)

  - **Supabase security remediation staged**: findings were re-verified live on November 5 (over-broad grants including TRUNCATE for anon and authenticated roles, RLS enabled but not forced, public profile SELECT exposing email and role, a self-updatable role column, and a stale shared-cases public policy). A least-privilege migration plus a full rollback plan is staged and awaiting owner approval - nothing has run against the database ([PR #27](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/27)).
  - **Brand assets wired**: the page and og:title were retitled to Greasy Dojo, favicon and OG image links were added, and asset paths were corrected to public/assets where the files live ([PR #28](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/28), [PR #29](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/29)).
  - **Final teal recolor**: the last hardcoded teal remnants (triage kicker, triage choices, and hero portrait frame) moved to fire orange ([PR #30](https://github.com/Chaotic-Minds-Collective/grease-dojo/pull/30)).
  - **Repository renamed**: the repo is now Chaotic-Minds-Collective/grease-dojo (was the-diagnostic-bay). Org automation targeting, repo descriptions, and the profile README were updated to match ([PR #8](https://github.com/Chaotic-Minds-Collective/.github/pull/8)).

  ### Collective HQ corporate site

  - **Phase 5 audit fixes**: Greasy Dojo rename applied across the site, Jojoa wording, root canonical tag, alt text, contact heading hierarchy, and nav order matching the homepage cards ([PR #7](https://github.com/Chaotic-Minds-Collective/chaotic-minds-collective/pull/7)).

  > Deployment verification, November 5 evening: Chaotic Solutions is live on Cloudflare Workers, and the latest Render deploys for Chaotic Command and Chaotic Gaming are live. The Grease Dojo GitHub Pages site and the corporate site's Pages deploy were not re-verified at publish time. Still zero Tally customer responses since the forms launched.

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
  - The GitHub repository kept its `the-diagnostic-bay` name through November 4; it was renamed to `grease-dojo` on November 5, and all new branding, copy, and public-facing pages use The Grease Dojo.

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
