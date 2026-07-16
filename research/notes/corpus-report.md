# Corpus Acquisition Report

Date: 2026-07-16

Goal: `goals/10-corpus-acquisition.md`

## Summary

Goal 10 acquired and normalized the legally accessible primary corpus for the
Gettysburg Address project. Raw files and normalized text are kept separate.
Hashes, retrieval dates, rights notes, acquisition methods, and verification
status are recorded in `research/data/source-register.csv`.

The required Gettysburg manuscript witnesses, ceremonial context, Lincoln
comparative texts, Everett materials, Wills invitation, and a limited public
reception sample are now preserved or explicitly blocked.

## Acquisition Method

Public web and repository sources were fetched with source-specific or
single-source tools:

- `scripts/fetch_source.py` for authorized public HTML/PDF downloads.
- `pdftotext` plus `scripts/normalize_text.py` for text-bearing PDFs.
- Local HTML extraction for institutional pages.
- `scripts/acquire_chronicling_page.py` for LOC Chronicling America page
  metadata and OCR payloads.
- `scripts/extract_chronicling_text.py` for normalized newspaper OCR text.

Network tools used a descriptive user agent from `.env`, conservative delays,
explicit output paths, and no CAPTCHA, paywall, authentication, or access-control
bypass.

## Acquired Corpus

Verified core Gettysburg witnesses:

- `SRC-0001` Nicolay Copy, LOC.
- `SRC-0002` Hay Copy, LOC.
- `SRC-0003` Everett Copy, ALPLM.
- `SRC-0004` Bancroft/Cornell Copy, Cornell.
- `SRC-0005` Bliss/White House Copy, Smithsonian PDF plus human
  transcription.

Verified ceremony and context:

- `SRC-0006` Everett oration and 1864 ceremony pamphlet.
- `SRC-0007` David Wills invitation.
- `SRC-0008` ceremony order/program, within `SRC-0006`.
- `SRC-0009` prayers, hymn, dirge, and benediction, within `SRC-0006`.
- `SRC-0012` Lincoln letter to Edward Everett.

Verified comparative Lincoln corpus:

- `SRC-0013` through `SRC-0028`, from Lyceum Address through Last Public
  Address.

Verified reception/discovery sources:

- `SRC-0040` Dickinson House Divided reception guide, discovery only.
- `SRC-0041` New-York Daily Tribune, November 20, 1863.
- `SRC-0042` Union County Star and Lewisburg Chronicle, November 27, 1863.

## Reception Limits

The public reception sample is intentionally limited. It includes an immediate
New York report/republication and a local Pennsylvania report with variant/noisy
wording. It does not support broad claims about national reception by itself.

`SRC-0011`, the Harrisburg Patriot/Patriot and Union criticism named in the
dossier, is acquired as a Dickinson House Divided derivative transcription while
the original newspaper image remains pending. The Dickinson record identifies
the source as `"A Voice from the Dead," The Patriot and Union (Harrisburg,
Pennsylvania), November 24, 1863, editorial`, page 1, transcribed by John
Osborne on 2013-11-15.

This is adequate for working reception analysis and source identification, but
not for final quotation-level verification. The original issue image should
still be acquired through GenealogyBank, Pennsylvania Newspaper Archive, a
library, or another lawful issue-level source.

Several Democratic or critical examples identified by Dickinson/Boritt are also
behind Newspapers.com, GenealogyBank, or NYT archive access. They should be
acquired later only through lawful access, with issue-level scans or OCR
preserved locally.

## Verification Notes

OCR-derived normalized texts are not quotation-final. Newspaper quotations and
the ceremony pamphlet require page-image checks before quotation-level use.

The Bliss Copy normalized text is a human transcription from the Smithsonian
manuscript image. It is approved for corpus acquisition, but quotation-level
claims should still check the manuscript page images and the transcription note.

## Repeatable Commands

Example LOC page acquisition:

```bash
set -a; source .env; set +a
.venv/bin/python scripts/acquire_chronicling_page.py \
  'https://www.loc.gov/resource/sn83030213/1863-11-20/ed-1/?sp=1' \
  research/corpus/primary/raw/SRC-0041-new-york-daily-tribune-1863-11-20-page-1 \
  --no-pdf
.venv/bin/python scripts/extract_chronicling_text.py \
  research/corpus/primary/raw/SRC-0041-new-york-daily-tribune-1863-11-20-page-1.fulltext.json \
  research/corpus/primary/normalized/SRC-0041-new-york-daily-tribune-1863-11-20-page-1.txt
```

The LOC PDF derivative for `SRC-0041` returned HTTP 403; the LOC page metadata
and full-text service were preserved instead.
