---
title: "Technology Usage Manifesto"
color: red
---

This document lays out a set of rules that I will follow in order to protect
myself from the pitfalls of modern technology. Note that if any rules conflict,
specific takes precedence over general.

## 0: Aims

The consequences of aims often have implicit assumptions and always have
limitations. I've tried to set them all out explicitly here.

### 0.1: Protect my personal data

Assumptions:

* No other party can be trusted to hold data securely.
* No proprietary software can be proven or trusted to not contain spyware.
* I can trust: modern encryption standards, containerisation, hardware.

Limitations:

* In reality hardware definitely can't be trusted (yet I have no choice but to trust it)
* Containerisation/hypervisors probably can't be trusted
* FOSS can still contain spyware, even though it is less common. Perhaps even
  FOSS software should be containerised.

Data Classification:

Secure: to my knowledge, there is no way another party can gain access to this
data. (Of course, that doesn't mean it's impossible, it almost certainly isn't)

Obscure: There are ways that this data could be accessed, but it is not likely
that it can be mined, due to some combination of obscurity, anonymisation, low
signal-to-noise ratio, low volume, and/or other technical constraints. Note
that modern neural networks have _incredible_ correlation power, and you should
not be surprised if this data eventually becomes public. Different sources of
obscure data should ideally be segregated such that correlations cannot easily
be made between them.

Public: The data is easily accessible by any party.

### 0.2: Have sovereignty over software I depend on

Assumptions:

* Having the rights to a piece of software's source code is both necessary and
  sufficient for sovereignty.
* These rights cannot be removed after they are given. This is correct for all
  FOSS licenses I know of, with GPL also protecting future derivatives.

Limitations:

* If software becomes unmaintained, you must be able to take over maintenance,
  or it doesn't matter anyway.

### 0.3: Fight against the usage of Big Data to influence public opinion

Comments:

* This can be used for both advertising, and, more worryingly, determining
  and/or influencing political beliefs.

### 0.4: Make a statement about the importance of FOSS

Assumptions:

* someone will care lol

Limitations:

* There is a fine line between sticking to your beliefs and being an ass.
* People might think that free software advocates are insane if I don't explain
  it well.

## 1: Internet connected software

Programs which only communicate with machines I control are not subject to
these conditions.

1.0) I will not consume media over a network through a means where different
usages can be correlated with each other. (Aim 3)

1.0) (comment) So I can't authenticate, I can't be personally identifiable, and
I must prevent fingerprinting (i.e. (1.2))

1.1) I will not access a remote server that requires authentication, unless I
accept that (a) my account may be breached or deleted at any time without
warning, and (b) any data I provide will be public knowledge. (Aims 1 and 2)

1.1) (comment) I may use a cloud storage provider I do not trust, provided that
the data is both mirrored to a local drive/NAS and either public or protected
with end-to-end encryption. File metadata must be hidden as well as file
contents.

1.2) If (1.1) applies but none of the data transferred can be linked to my
identity, the data shall be considered "obscure" rather than public.

1.3) Unless all transferred data is public, I will only access remote servers
through Tor or similar, to prevent fingerprinting. (Aim 1)

1.3) (comment) Further anti-fingerprinting measures should also be taken when
possible, e.g. modifying user agent strings to the most common option. (Aim 1)

1.4) I will not grant a remote server access to any sensing peripherals (e.g.
microphone or camera), unless it is verifiably protected by client-side
end-to-end encryption. (Aims 1 and 3)

1.5) If free (libre) or trivial code is downloaded from a remote server and
then immediately executed (e.g. JavaScript), only *the source itself* should be
whitelisted, not the remote server, to prevent a bait-and-switch scenario.
(Aims 1 and 2)

## 2: Software

In this section, an "untrusted sandbox" (US) refers to a sandbox used for
running untrusted software, and can be either a container on a hardened kernel,
a VM, or a dedicated untrusted machine. Note that a dedicated machine is far
more secure than the other two options.

2.0) I will not depend on any proprietary software. (Aim 2)

2.0) (comment) I may use proprietary software for ephemeral applications, or
when a suitable alternative is easy to come by and the switching cost is
manageable on short notice.

2.1) Proprietary software must be run in a US. (Aim 1)

2.2) USes can have either read-only access to private data, or a network
connection, but never both at the same time. (Aim 1)

2.3) A US that has previously had network access can later have access to
private data, but a US that has previously had access to private data can never
have network access. (Aim 1)

2.4) USes should be reverted to a clean state after every use. (Aim 1)

## 3: Firmware

3.0) I will use proprietary firmware only if no FOSS firmware exists, and if
having no firmware would render the device useless (Aims 1, 2, and 4)

3.1) I will not purchase a device that requires proprietary firmware unless
there is no other suitable device in that class (Aims 1, 2, and 4)

3.2) When transitioning from a device with proprietary firmware to a device
with FOSS firmware, I will assume all data on the original device is
compromised and malicious. (Aim 1)

## 4: Other people

4.0) I will not be pressured into using software without first taking the time
to consider this manifesto.

4.1) If I am pressured to contravene this manifesto against my will, and I
cannot resist, I will seek solutions that contravene the aims in descending
order. If Aim 1 must be contravened, it should be done in a way that
compromises the smallest amount of the least sensitive data possible.

4.2) When transferring data to a person who does not comply with this manifesto
or a similar one, but nonetheless through a method which, on my end, does not
contravene this manifesto, I will assume the data becomes "obscure" (unless it
is already public). (Aims 1 and 4)

4.3) I will not use a proprietary messaging service, unless it can be
adequately bridged to a FOSS client. (Aims 1 and 2)

4.4) I will not use a messaging service unless it has verifiable FOSS
end-to-end encryption, except when the messages are public (this includes email
unless PGP is used) (Aims 1 and 4)

4.4) (comment) i.e. components of the communication channel can be
proprietary/untrustable, as long as the E2E encryption is FOSS. Ideally the
entire communication channel would be decentralised in order to protect
metadata (e.g. Matrix), but this is not a requirement.

## 5: Other computers

5.0) I may use computers I do not trust, but I must assume any data relating to
my usage of the system is public - unless my identity can be concealed, in
which case the data will be considered "obscure". (Aim 1)

## 6: Workplace software

6.0) An organisation I work for is responsible for the work I do, but not my
personal data. I need not apply this manifesto to workplace computing, except
where it applies to personal data.

6.0) (comment) A clear segregation should be made between personal computing
and workplace computing.

6.1) I will, where possible, encourage organisations I work for to apply
similar goals to their internal practices.

## Addendum: current changes that need to be made

| Software                     | Solved      | Current Replacement                                                       |
|------------------------------|-------------|---------------------------------------------------------------------------|
| Audio Consumption (Spotify)  | ✅ 2022-12  | ~~CD ripping? direct purchasing?~~ Rip from Spotify into custom system    |
| Traditional TV/movies        | ✅ 2024-08  | Rip from various places into custom system                                |
| YouTube                      | ✅ 2024-08  | Selfhosted CloudTube plus rip from YouTube and Nebula into custom system  |
| Cloud Storage (backup)       | ✅ 2022-04  | Borg + NAS + replication to Backblaze                                     |
| Cloud Storage (continuous)   | ✅ 2023-01  | ~~VPS/equivalent + E2E encryption +~~ NAS + SFTP/NFS                      |
| Gaming                       |             | Public metadata + containerised Steam? Hmm.                               |
| MessageEase keyboard         | ✅ 2023-01  | ~~Build my own~~ use qwerty and be sad                                    |
| DnD beyond                   | ✅ 2022-04  | ~~Find alternative? Build my own?~~ Use paper                             |
| Google Photos                | ✅ 2022-04  | just folders on NAS lol                                                   |
| Social media                 | ✅ 2025-01  | ~~Just don't use? Fediverse stuff? Selfhosted FOSS frontend?~~ Minimise use for consumption, make all posts public |
