---
layout: post
title: "Using DigitalOcean with Docker"
published: true
---

### "Why does Docker download all of those files?"

[Sign up to DigitalOcean](https://www.digitalocean.com/?refcode=b83d4ac48a52)


##Create Droplet on [DigitalOcean](https://cloud.digitalocean.com/)


**Droplet Hostname:**
arbiterofcool

**Select Size:**
$5/mo

![Create Droplet](/images/do-create-droplet.png)



**Select Region:**
San Francisco

![Select Region](/images/do-select-region.png)



**Select Image:**
Applications, Docker 1.2.0 on Ubuntu 14.04



![Select App](/images/do-select-app.png)

**Add optional [SSH Keys](https://cloud.digitalocean.com/ssh_keys):**
schatman

![Last Step](/images/last-step.png)

**On command line:** 
ssh root@(DROPLET_IP)
