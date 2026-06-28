---
title: "She Gave Me a Paper Form. I Built an App."
subtitle: "A doctor asked me to track my blood pressure on paper for a few weeks. I built the app instead. It took an afternoon, and it does the one job paper had, better."
date: 2026-06-28
description: "At a checkup the doctor reached for a paper form to track my blood pressure. I built bplog instead: a local-first PWA with trends and a printable doctor report, open source, built in an afternoon with AI. The cost of a personal tool dropped below the cost of the friction."
cover: /assets/img/2026-06-28-paper-form-built-an-app.png
coverAlt: "A paper blood-pressure form on a dark desk under warm amber light giving way to a glowing phone screen showing a clean rising trend chart, teal rim light, brushstroke texture and soft bloom."
---

At my last checkup, my blood pressure read a little high. Not alarming, but enough. The doctor wanted a few weeks of data before deciding anything, so she asked me to take two readings a day and write them down. Then she reached for a pad to hand me a paper form.

I almost took it. Then I stopped. Why paper?

## The math flipped

For most of my life, paper was the right answer. Building an app to track five numbers would have meant days of setup, a backend, a login screen, a database, a deploy. All of it out of proportion to the task. Paper won because the alternative was absurd.

The math is different now. The setup is what collapsed, and with it the whole reason to reach for the pad.

## What I built

I built bplog. It is a blood-pressure logging app for your phone. Two readings a day, morning and evening, with a tap to mark how you felt. It runs in the browser, installs to your home screen, and works offline. The numbers stay on your device. It is live at [bplog.dynaum.com](https://bplog.dynaum.com) and open source under MIT.

## An afternoon, not a project

Here is the part worth dwelling on. It took an afternoon.

Not because it is a trivial app. It charts trends over 7, 30, or 90 days. It classifies every reading against the American Heart Association ranges. It generates a printable report for the doctor. It exports and restores backups. It took an afternoon because I did not write most of it by hand. I described what I wanted, and the model produced the scaffolding, the components, the chart wiring, the service worker, the tests. React, Vite, TypeScript, Material 3. On my own I would have spent the first day relearning how to configure a PWA. The model had it running before lunch.

This is the idea I keep coming back to in [Build Your Own Tools](/posts/2026-05-28-build-your-own-tools/). The cost of a custom tool used to be the reason you tolerated the friction instead. That cost fell through the floor. When building the right thing is an afternoon, "live with the paper form" stops being the rational choice.

## Fast did not mean sloppy

The worry with an afternoon app: it is a toy. This one is not.

bplog is local first by design. Your readings live in your browser's storage on your own device. No account, no server, no tracking, no upload. The app makes no backend calls with your data at all. The paper form had one quiet virtue, it was private, and most health apps trade that away. This one keeps it.

It is also accessible. It targets WCAG 2.1 AA, ships an automated accessibility check in the test suite, keeps color from being the only signal, and gives the chart a text-table equivalent for screen readers. The domain logic, the classification and the statistics, is unit tested with no UI in the way.

None of it is exotic. It is what a competent app should do. The point is that an afternoon build cleared that bar, because the model carries the breadth I would otherwise cut to save time.

## The report that beats paper

Paper had one job: hand the doctor a record at the next visit. It is bad at it. A notebook is a column of scribbles. A photo of the notebook is worse. The doctor squints, you read numbers aloud, the trend stays invisible.

bplog has a doctor report. One page, print or save as PDF: the summary, the chart, a category breakdown, and a full table of every reading. The doctor reads it in seconds and sees the shape of the last month, not a pile of digits. The tool wins at the exact job paper was for.

## The default should move

She reached for paper because paper is the default for "track this yourself." That default is a leftover from when the alternative was expensive. It is not anymore.

I am not saying build an app for everything. Plenty of times paper or an existing app is the right call, and I reach for both. I am saying the threshold moved, and most people have not updated where they think it sits. When the friction is a form you will lose and a photo your doctor cannot read, and the fix is an afternoon, the honest answer is to build the fix.

## Use it

bplog is free, open source, and lives entirely on your device. If a doctor ever hands you a paper form for your blood pressure, you have another option.

Open [bplog.dynaum.com](https://bplog.dynaum.com) on your phone, add it to your home screen, and log a reading. The code is on [GitHub](https://github.com/dynaum/bplog) if you want to read it, fork it, or make it your own.
