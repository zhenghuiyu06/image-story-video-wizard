# City Archives production profile

Use this profile only when the user invokes `城事档案`, asks for a regional historical figure episode, or frames a topic as how one person shaped a city. Record `production_profile = city-archives-v1` in project state. These are defaults, not permission to skip the workflow's script, pilot, preview, or final acceptance gates.

## Editorial contract

- Build the episode around a specific person and a demonstrable effect on one city or region. Prefer a concrete institution, landscape, industry, trade system, educational project, or urban transformation over a general biography.
- Validate the topic with official publications, archives, local chronicles, museums, academic work, or other reliable sources. Keep source links and distinguish documented facts from later stories; label unresolved claims `待考` and do not turn them into certain narration.
- Default platform and form: Douyin, 9:16, 1080 x 1920, eight to twelve minutes, one narrator, audio first, and an economical ten-to-twelve-second image cadence.
- Learn benchmark topic logic, hook, escalation, transitions, language, and ending. Never copy finished wording or media.

## Voice and channel identity

- Open with exactly `欢迎来到今天的城事档案。` and move directly into the factual hook. Never include production notes such as `屏幕出现` or `画面展示` in narration, subtitles, prompts, or overlays.
- Prefer a slightly fast body delivery. When current Doubao access is verified, audition or reuse the confirmed `儒雅逸辰` voice. If it is unavailable, use a locally verified alternative only after a short audition; do not claim a provider or voice was used without an actual call.
- Default to no background music. If the user later requests music, return to the MUSIC gate and keep narration dominant.

## Visual production

- Preserve the three-to-five-image pilot and any required face/full-body anchor confirmation before production generation.
- When `image_generation_mode = assistant` and the current host exposes image generation, the Skill owns production after pilot approval. Explain material cost once, then generate one prompt and one image per call.
- Every individual prompt must repeat the complete frozen style plus era, geography, identity/reference use, composition, 9:16 output, lower twenty-percent subtitle-safe area, camera-move margin, modern-element exclusions, and readable-text/watermark exclusions. Never rely on a separate shared-constraints block.
- Save by storyboard shot ID, never by model return order. Use face and full-body anchors only for shots that need the recurring person's identity.
- Plan production in batches of ten; the final batch contains the remainder. Run `scripts/image_batch_plan.py STORYBOARD.csv --size 10` when a deterministic plan is useful.
- After each batch, inspect narration match, identity, clothing and era, regional geography, architecture and transport, style continuity, modern objects, readable text or watermark, framing, and subtitle-safe space.
- Retry a critical failure once. Critical failures include wrong region or terrain, wrong city type, modern clothing or infrastructure, identity replacement, serious era conflict, readable text, logo, or watermark. Move the failed original into `images/revisions/` and keep only the accepted version in the formal directory.
- Record minor object inaccuracies without endless retries. After the single retry, flag any remaining critical issue for the final whole-set review.
- Write `review/IMAGE_BATCH_NN_QC.md` after each batch and continuously update `images/GENERATION_LEDGER.md`. Do not ask for approval between production batches; present all unresolved items together after final ASSET_QC.

## Preview and master

- Use the first image throughout a roughly one-to-one-and-a-half-second light antique-paper page-turn introduction. Display only `欢迎来到今天的城事档案` in the opening visual.
- Keep subtitles in the lower half on a small local backing plate, never a full-screen dark veil. Put important dates at the upper-left or middle-left with a short event label and avoid subtitle overlap.
- Apply restrained push-in, pull-out, and horizontal movement to still images. Build a browser preview first and require explicit approval before final render.
- Default master: 1080 x 1920, 30 fps, H.264 video with AAC audio. Validate duration, streams, representative frames, black frames, and audio continuity.
- Deliver only the high-definition master to the current user's Downloads folder. Do not generate a mobile-compatible derivative and do not delete older derivatives. Keep status `已做待验` until the user accepts the master.

## Authorization boundary

Autonomous image production authorizes only the confirmed image count and one necessary retry per critical failure after pilot approval. It does not authorize publishing, channel changes, paid services beyond the disclosed production scope, or skipping the preview and final acceptance gates. Never store or publish credentials, tokens, session URLs, raw private conversations, or private machine paths.
