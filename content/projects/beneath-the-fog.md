---
title: Beneath the Fog
subtitle: Narrative-Driven RPG Prototype
excerpt: A fully playable JRPG slice featuring quests, dialogue systems, and turn-based combat, created in Unity.
technologies: [Unity, C#, Narrative Design, Systems Design]
order: 4
image: ../content/assets/images/beneath-the-fog/Thumbnail.png
---
<div align="center">
<iframe width="720" height="480"
src="https://www.youtube.com/embed/E1O0pUW1cFI?autoplay=1&mute=1">
</iframe>
</div>

**Genre:** 2D RPG

**Role:** Solo Game Designer and Developer

**Engine:** Unity

**Timeframe:** 4 months

# Overview

*Beneath the Fog* is a narrative-driven RPG slice built in Unity, centered on two boys navigating a world slowly overtaken by a mysterious fog. As they uncover the truth behind the sickness and madness spreading through their village, players make choices that shape how the story unfolds.

The prototype includes branching dialogue built with Ink, a turn-based combat system, and a dynamic quest structure. Designed as a systems-focused production project, it explores how narrative and mechanics can work together to reflect player intent, memory, and consequence.

### Concept & Early Development

*Beneath the Fog* started with a question: what happens to a world that’s slowly being swallowed by fog? I imagined two boys growing up in a quiet village, trying to understand what the fog was doing to the people around them, and what it might be doing to them, too.

I began with a brainstorm in mind map form with the guidance of my professor and bounced ideas off classmates as they formed. I knew i wanted it to be really rooted in story, and that I wanted the systems to play off the story well. Though I orignally brainstormed it as a 3D game, I changed it to 2D for scope purposes. From there, I built it out into a pitch deck. I then scoped out a vertical slice focused on system interactions: branching dialogue, turn-based combat, a small inventory system, and an event-driven quest system, all working together to reflect the player's choices and path.

<div align="center">
<img src="../content/assets/images/beneath-the-fog/Mindmap.png" alt="Mind Map" style="width:75%;" />
</div>

### Production Focus

Built for a production-focused senior class, this game pushed me to design, build, and iterate on interlocking systems from scratch. Major components included:

* Branching dialogue built in Ink and integrated into Unity
* A turn-based combat system connected to quests and narrative state
* A dynamic event-driven quest and inventory system
* A custom UI system reflecting world and player state

Each piece had to communicate with the others, forming a responsive slice where player actions shaped what happened next.

### Fog Meter

One of the most ambitious systems I planned—but wasn’t able to fully implement—was a global “Fog Meter” mechanic. The idea was for the fog to affect more than just visuals. It would function like a slow-burn status system: reducing magic access, restricting dialogue, and eventually forcing the player to collapse if they didn’t manage their exposure.

I built out a complete logic flow (see diagram below) showing how fog exposure would interact with combat, narrative, and environment systems. While I didn’t have time to integrate it into the playable build, designing this helped me think through edge cases, player agency, and recovery loops. It’s something I’d love to explore in a future version of the game.

<div align="center">
<img src="../content/assets/images/beneath-the-fog/Fog_Flow_Chart.png" alt="Fog Flow Chart" style="width:75%;" />
</div>

### Combat & UI

Combat included turn selection, magic resource tracking, and quest-triggered conditional logic. I began with wireframes and refined the UI through testing, making sure it was readable and responsive. Combat outcomes could unlock or change quests and future dialogue branches.

<div align="center">
<img src="../content/assets/images/beneath-the-fog/combat_mockup.png" alt="Combat Mockup" style="width:75%;" />
</div>

### Challenges & Iteration

The biggest challenge was getting everything to talk to everything else. Syncing Ink with Unity required writing custom bridge logic to track variables and lock or unlock events dynamically. Combat and quests also had to stay in sync with dialogue states and inventory checks. I spent a lot of time untangling bugs where one system didn’t update another correctly.

To keep things modular, I used an event-driven structure and broke tasks into smaller, testable systems. I also refined UI and feedback loops based on testing, learning how much clarity matters when branching logic is involved.

### What I Learned

* Dialogue systems only work with strong logic behind them
* Unity and Ink pair well, with enough bridge code
* Modular systems save you later headaches
* Event-driven architecture helps keep complex systems connected
* UI clarity is just as important as narrative clarity
