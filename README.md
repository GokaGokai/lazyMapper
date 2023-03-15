# Lazy-Mapper  
   
<img src="https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/showcase.PNG" alt="drawing" width="700"/>
<img src="https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Custom.gif" alt="drawing" width="500"/>


<!-- TABLE OF CONTENTS -->
### Table of Contents
<ul>
<li><a href="#about">About</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#showcase">Showcase</a></li>
</ul>

<br>

<!-- GETTING STARTED -->
## About
### Current Features
Generate different kinds of Long Stream Maps for any maps.    
You only need to drag *lazyMapper.py* to the song folder and double-click it.  
The first note starts on the first timing point and the last note ends on the last timing point.  
The template folder includes WE LUV LAMA in various difficulties. (space aim levels)

   
### Future Plans
-GUI Version  
-No need to drag *lazyMapper.py* to the song folder   
-Adding the possibility for breaks (Use editor for now)  
-Adjusts to changing BPM maps and able to choose the timing points  
-Possibility for different patterns such as Jumps, Squares, Corners, Bursts, Triplets, or Quadruplets..  
-On-the-fly chosen CS, AR, OD, HP, inverted.. (Use editor for now)

<br>   

For those who are in a sigma grindset like khz's, I'll be happy if it helped someone. But it's mostly for myself for now.  
  
   

### Prerequisites

I believe you only need python3.

<br>

<!-- USAGE EXAMPLES -->
## Usage 
Download the <a href="https://github.com/GokaGokai/lazyMapper/releases/tag/0.1.1">latest release</a> or download the zip by clicking the green button on the page (Code, scroll up) or clone my repo.  
  
Open Osu!, go to the editor, and choose a map.  
Open Song Folder (File, top left), and copy *lazyMapper.py* inside.  
*(Optional)* If you want a custom template, drag it as well in here.


<img src="https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/guide.PNG" alt="drawing" width="550"/>

<br>   

Upon double-clicking *lazyMapper.py*, select one of the map difficulties. (I would mostly look based of the OD personally)   
  
```
----------

lazyMapper

----------
0 - DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [S1.0].osu
1 - xi - Wish upon Twin Stars (Chaoslitz) [BASIC].osu
2 - xi - Wish upon Twin Stars (Chaoslitz) [EXHAUST].osu
3 - xi - Wish upon Twin Stars (Chaoslitz) [Gaia's ADVANCED].osu
4 - xi - Wish upon Twin Stars (Chaoslitz) [HYPER].osu
5 - xi - Wish upon Twin Stars (Chaoslitz) [NOVICE].osu
6 - xi - Wish upon Twin Stars (Chaoslitz) [Wish].osu

Which map to parse from? [0-6]
(Only for stats such as CS, AR, OD, HP..)
```
Prompt Example: 6  
<br>   

```
---
0 - Square
1 - Circle
2 - Small Square
3 - Custom

What kind of map do you want to generate? [0-3]

```
Prompt Example: 3 (The third prompt will only show if you select Custom)  
<br>   

```
---
0 - DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [S1.0].osu
1 - xi - Wish upon Twin Stars (Chaoslitz) [BASIC].osu
2 - xi - Wish upon Twin Stars (Chaoslitz) [EXHAUST].osu
3 - xi - Wish upon Twin Stars (Chaoslitz) [Gaia's ADVANCED].osu
4 - xi - Wish upon Twin Stars (Chaoslitz) [HYPER].osu
5 - xi - Wish upon Twin Stars (Chaoslitz) [NOVICE].osu
6 - xi - Wish upon Twin Stars (Chaoslitz) [Wish].osu

Select the osu file you want to copy from. [0-6]
(Assuming you dragged it in the same folder already)
```
*(Optional)* Prompt Example: 0 (Using the template in my github)  
<br>   

Done!  
  
You should be able to see the new map in the folder, which was, in this example,    
*xi - Wish upon Twin Stars (Chaoslitz) [lazyMapperCustom (DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [S1.0].osu)].osu*  

<br>   

Just go back to Osu! and find it. (Refresh by going in and out)   

<br>   

If you have any questions, discord: GokaGokai#7048

<br>   

## Showcase
Using *lazyMapper.py* on <a href="https://osu.ppy.sh/beatmapsets/242462#osu/559673">Wish upon Twin Stars</a>

### Square


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Square.gif)

### Circle


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Circle.gif)

### Small Square


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/SmallSquare.gif)

### Custom
(Using the template *DJ Sharpnel - WE LUV LAMA 2 (-Tynamo) [S1.0].osu*)


![](https://github.com/GokaGokai/lazyMapper/blob/main/Ressources/Custom.gif)
