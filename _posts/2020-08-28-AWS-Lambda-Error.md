---
layout: post
title: AWS Lambda error fix
category: server
tags: aws lambda error env tip
---

# Everything was rolling along...
We have a handful of lambda functions running on AWS. Everything was running as it should until this morning.

`ERROR: Could not install packages due to an EnvironmentError: [Errno 28] No space left on device`

It was just good luck that I was updating a lambda at the same time that this error showed up and propagated through all our lambdas. I should probably have some sort of alert set up for when this happens.

Our tech lead figured it out quickly -- he referenced [this page](https://epsagon.com/tools/free-lambda-code-storage-exceeded/) and made some updates. I triggered the lambda to test it, and all was well.

