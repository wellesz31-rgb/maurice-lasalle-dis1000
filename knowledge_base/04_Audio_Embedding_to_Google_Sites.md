# Audio Embedding to Google Sites
## DIS 1000 Teaching Assistant Knowledge Base

---

## Overview: The Complete Pipeline

After exporting a WAV file from Cakewalk, students need to:
1. Upload the WAV file to Google Drive
2. Set sharing permissions so the file is accessible
3. Get a shareable link
4. Embed that link into their Google Site

**Why this process?** Google Sites doesn't allow direct WAV file uploads. Instead, you upload to Google Drive and embed from there.

---

## Step 1: Upload WAV File to Google Drive

### Finding Your Exported File

First, locate the WAV file you exported from Cakewalk.

**Common locations:**
- The folder you specifically chose during export
- Your Cakewalk project folder: `Documents/Cakewalk Projects/[ProjectName]/Audio/`
- Your Downloads folder (if that's where you saved it)

**Tip:** If you can't find it, search your computer for `*.wav` files modified today.

### Uploading to Drive

**Method 1: Via Web Browser**
1. Open your web browser
2. Go to https://drive.google.com
3. Sign in with your Google account
4. Navigate to a folder or create a new folder for your DIS 1000 audio files
   - **Recommended:** Create a folder called "DIS 1000 Audio" or similar
5. Click the **+ New** button (or right-click in the folder)
6. Select **File upload**
7. Browse to your WAV file location
8. Select the file and click **Open**
9. Wait for the upload to complete (a notification appears when done)

**Method 2: Drag and Drop**
1. Open Google Drive in your browser
2. Navigate to your desired folder
3. Open your file explorer (separate window)
4. Locate your WAV file
5. Drag the file from your file explorer into the Google Drive browser window
6. Drop it—the file uploads automatically

**Upload time:** A 2-3 minute WAV file (20-30 MB) typically uploads in under a minute on a decent internet connection.

---

## Step 2: Set Sharing Permissions

**Critical step!** If you skip this, your instructor and classmates won't be able to hear your audio when it's embedded in your Google Site.

### Making the File Shareable

1. In Google Drive, find your uploaded WAV file
2. **Right-click** on the file (or click the three-dot menu ⋮ next to it)
3. Select **Share** from the menu
4. A sharing dialog appears

### Configuring "Anyone with the Link"

In the sharing dialog:

1. Under **General access**, you'll see the current setting (likely "Restricted")
2. Click on **Restricted** to open a dropdown menu
3. Select **Anyone with the link**
4. A role dropdown appears next to it—make sure it's set to **Viewer**
   - Viewer is correct—people can listen but not edit
5. Click **Done**

**What this does:** Anyone who has the link (including when it's embedded in your Google Site) can access and play the audio file.

**Visual reference:** See the screenshots from Images 1-2 in the original screenshot set showing this process.

---

## Step 3: Get the Shareable Link

### Copying the Link

After setting permissions:

1. **Right-click** on the file again (or click the three-dot menu ⋮)
2. Select **Share** (or you might see **Copy link** directly—either works)
3. In the sharing dialog, look for a **Copy link** button at the bottom
4. Click **Copy link**
5. The link is now copied to your clipboard

**The link will look something like:**
```
https://drive.google.com/file/d/1KnIsgcDn_55c_YAnKHvAaE9tS8t399kS/view?usp=sharing
```

**Important:** This is a Google Drive link, not a direct file link. Google Sites can embed Google Drive links directly.

---

## Step 4: Embed in Google Sites

### Navigating to Your Site

1. Go to https://sites.google.com
2. Open your DIS 1000 portfolio site (or create it if you haven't yet)
3. Navigate to the page where you want to embed the audio
   - For Studio Work assignments: go to your **Studio Work** section page
   - Create a new sub-page if needed for this specific assignment

### Using the Embed Function

**Option A: Embed by URL (Recommended)**

1. Click where you want the audio player to appear on your page
2. On the right panel, click the **Insert** tab
3. Click **Embed** (icon looks like `<>`)
4. A dialog box appears with two tabs: "By URL" and "Embed code"
5. Make sure **By URL** tab is selected
6. **Paste the Google Drive link** you copied earlier into the text field
7. Click **Insert**

**Result:** An embedded audio player appears on your page!

**Visual reference:** See screenshot Image 3 from the original set showing the Embed dialog.

### What the Embedded Player Looks Like

After embedding, you'll see:
- A rectangular frame on your page
- Inside it: Google Drive's audio player interface
- Play/pause button
- Timeline/progress bar
- Volume control

**Visitors to your site can:**
- Click play to listen to your composition
- Scrub through the timeline
- Adjust volume
- They do NOT need to download the file or leave your site

### Troubleshooting Embed Issues

**"The embed isn't showing up"**

**Possible causes:**
1. The file sharing permissions are not set to "Anyone with the link"
2. You pasted the wrong link format
3. Google Sites is having a temporary issue

**Solutions:**
- Go back to Google Drive and verify the file is set to "Anyone with the link" → Viewer
- Try copying the link again and re-embedding
- Make sure you're pasting the full link (starts with `https://drive.google.com/file/d/...`)
- Wait a moment—sometimes it takes a few seconds to load

**"The player shows but says 'No preview available' or won't play"**

**Possible causes:**
1. Sharing permissions are incorrect
2. The file is corrupted
3. The file format is wrong (not WAV)

**Solutions:**
- Double-check sharing permissions (this is the most common issue)
- Try playing the file directly in Google Drive—if it doesn't play there, re-export from Cakewalk
- Verify you exported as WAV (not MP3 or another format)

**"The player is too big/too small"**

**Adjustment:**
- Click on the embedded player in edit mode
- Blue handles appear around the edges
- Click and drag to resize
- Or use the toolbar options to adjust size/alignment

---

## Step 5: Verify and Publish

### Test the Embed

Before publishing, test that everything works:

1. In Google Sites edit mode, click the **Preview** button (tablet/phone icon in top toolbar)
2. Your site opens in preview mode
3. Navigate to the page with your embedded audio
4. Click the **play button** on the audio player
5. Verify that your composition plays correctly

**If it doesn't play in preview:**
- Go back and check sharing permissions
- Make sure you embedded the correct link
- Try refreshing the preview

### Publish Your Site

**Critical step:** Remember from the syllabus—you must re-publish every time you make changes!

1. Click the **Publish** button in the top-right corner
2. Review your site name and URL (should already be set)
3. Confirm sharing settings: "Anyone with the link"
4. Click **Publish**

**Your changes are now live!** Your instructor can now access your site and hear your composition.

---

## Common Workflow Issues

### "I embedded the file but my instructor says they can't hear it"

**Most common cause:** You forgot to publish after embedding.

**Solution:**
- Make sure you clicked **Publish** after embedding the audio
- Check that the site is set to "Anyone with the link" (not restricted)
- Share your site URL with your instructor again to confirm they're accessing the right link

### "I need to replace the audio file (I made a mistake)"

**Two approaches:**

**Option 1: Replace the file in Google Drive (keeps the same link)**
1. In Google Drive, delete the old WAV file
2. Upload the new WAV file with the EXACT same name
3. Set sharing permissions
4. The embedded link should now play the new file

**Option 2: Upload new file and re-embed (more reliable)**
1. Upload the new WAV file to Google Drive (can have a different name)
2. Set sharing permissions and copy the link
3. In Google Sites, delete the old embedded audio player
4. Embed the new link
5. Publish

### "I uploaded the file but embedding isn't working"

**Checklist:**
1. ☐ File is uploaded to Google Drive
2. ☐ File sharing is set to "Anyone with the link"
3. ☐ You copied the shareable link (not just the file name)
4. ☐ You used the Embed function (not just pasting the link as text)
5. ☐ You're embedding a Google Drive link (starts with `https://drive.google.com/file/d/...`)

**Go through this checklist step by step to identify where the problem is.**

### "Can I embed multiple audio files on the same page?"

**Yes!** You can embed as many as needed.

**How:**
1. Upload all your WAV files to Google Drive
2. Set sharing permissions for each
3. Copy each file's link
4. Embed them one at a time on your page
5. They'll stack vertically by default
6. You can add text boxes between them to label each one

**Example use case:** If an assignment asks you to create multiple short compositions, you can embed all of them on the same page.

---

## Alternative: Embedding from YouTube

Some students prefer to upload audio to YouTube (as an audio-only video) and embed from there.

**This is acceptable for DIS 1000**, but has extra steps:

### Quick YouTube Process

1. Create a simple video with your audio (use free tools like Windows Video Editor)
2. Upload to YouTube (can set to Unlisted so it's not public)
3. Copy the YouTube video URL
4. Embed in Google Sites using the same Embed → By URL process

**Pros:**
- YouTube player is familiar to everyone
- No Google Drive storage limits
- Can add a static image to make it more visually interesting

**Cons:**
- Extra step of creating a video file
- Takes longer to upload and process
- More complex than the Google Drive method

**Recommendation:** Stick with Google Drive for simplicity unless you have a specific reason to use YouTube.

---

## Tips for Success

### Organize Your Google Drive

**Create a folder structure:**
```
DIS 1000 Audio/
├── Week 1 - Sound Composition/
├── Week 2 - Texture Composition/
├── Week 3 - Beats and Loops/
etc.
```

**Why:** When you have 10+ audio files, organization prevents confusion.

### Name Files Clearly

**Bad:** `audio.wav`, `final.wav`, `composition1.wav`

**Good:** `Turner_Week1_SoundComp.wav`, `Turner_Week3_Beats.wav`

**Why:**
- Easy to identify which file is which
- Instructor can easily identify your work
- Less chance of uploading the wrong file

### Upload Early

**Don't wait until the last minute!**

If you encounter upload or embedding issues:
- You'll have time to troubleshoot
- You can ask for help before the deadline
- Internet issues won't cause you to miss the deadline

**Good habit:** As soon as you export from Cakewalk, upload to Drive and embed in your site right away.

### Test on Multiple Devices

After publishing, try accessing your site from:
- Your computer
- Your phone
- A different browser

**Why:** Ensures your embed works universally and your instructor will be able to access it.

---

## Summary: The Complete Audio Embedding Workflow

1. **Export from Cakewalk** as WAV (see Document 3)
2. **Upload WAV to Google Drive**
   - Go to drive.google.com
   - Upload your file to a dedicated folder
3. **Set sharing permissions**
   - Right-click file → Share
   - Change to "Anyone with the link" → Viewer
   - Click Done
4. **Copy the shareable link**
   - Right-click file → Copy link (or use the Copy link button in Share dialog)
5. **Embed in Google Sites**
   - Open your site, navigate to the correct page
   - Click Insert → Embed → By URL
   - Paste the Google Drive link
   - Click Insert
6. **Preview to test**
   - Click the Preview button
   - Make sure audio plays
7. **Publish your site**
   - Click Publish
   - **Remember: You must publish for changes to be visible!**
8. **Verify**
   - Visit your published site in a new browser tab
   - Test that audio plays
   - Submit your site link to your instructor

**That's it!** This process becomes quick and automatic after doing it once or twice.

---

## When to Ask for Help

### Good questions for the teaching assistant:

- "I uploaded my file to Google Drive but I don't know how to set sharing permissions"
- "I embedded the audio but it's not playing—what should I check?"
- "My file says 'No preview available' when I try to embed it"
- "How do I get the shareable link from Google Drive?"
- "I published my site but my instructor says they can't hear my audio"

### When to contact your instructor:

- Assignment questions (what you're supposed to create)
- Grading questions
- Extension requests
- Questions about artistic/analytical content

**The teaching assistant helps with the technical process of uploading and embedding.**

**The instructor helps with course content and creative direction.**

---

## Final Reminders

### Always Publish After Making Changes

**From the syllabus:** "You must re-publish your site any time you add to it or make changes: inaccessible work will be considered late."

**Make this a habit:**
1. Make changes to your site (add content, embed audio, etc.)
2. Click **Publish** immediately
3. Verify the changes are live by visiting your published site URL

### Sharing Permissions Are Critical

If your file is set to "Restricted" instead of "Anyone with the link":
- Your instructor cannot access it
- Your embedded audio won't play
- Your work will be considered incomplete/late

**Always double-check sharing settings!**

### Keep Original Files

**Don't delete:**
- Your Cakewalk project files (.cwp)
- Your exported WAV files

**Why:**
- You might need to revise and re-export
- You'll want these for your portfolio beyond this course
- Instructor might request changes

**Good practice:** Back up your DIS 1000 work to an external drive or cloud storage.

---

## You've Got This!

The audio embedding process seems complicated the first time, but after you do it once or twice it becomes second nature:

1. Export WAV from Cakewalk
2. Upload to Google Drive
3. Set to "Anyone with the link"
4. Copy link
5. Embed in Google Sites
6. Publish

**That's the whole workflow.** Six steps, and you're done!

If you get stuck, use the teaching assistant for technical questions, and don't hesitate to ask for help early rather than waiting until the deadline.
