---
title: Neon Grid
date: 2025-03-02
rank: 0
summary: neon grid
description: neon grid
toc: false
readTime: false
autonumber: true
math: true
tags:
  - shaders
  - GLSL
showTags: true
hideBackToTop: false
---

<iframe width="700" height="700" frameborder="0" src="https://www.shadertoy.com/embed/wfXSD4?gui=true&t=0&paused=false&muted=false" allowfullscreen></iframe>

Techniques: Coordinate repetition with mod, Shaping function

View on [**ShaderToy**](https://www.shadertoy.com/view/wfXSD4)

```glsl
#define PI     3.14159265
#define TWO_PI 6.28318530

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 st = fragCoord.xy/iResolution.xy;

    // repeat coordinate
    float repeat_count = (sin(iTime+1.*PI)+1.)*1.5+1.;
	float spacing = 1./repeat_count;
    float repeat_offset = -0.5;
    
    st.x = mod(st.x+repeat_offset, spacing)/spacing;
    st.y = mod(st.y+repeat_offset, spacing)/spacing;
    
    // shaping
    float pow_expo = (sin(iTime*2.)+1.)*0.4;
    float offset = (0.5+0.25) * PI;
    st.x = 1.-pow(abs(sin(PI*st.x/2.+offset)), pow_expo);
    st.y = 1.-pow(abs(sin(PI*st.y/2.+offset)), pow_expo);

    vec2 mask = vec2(length(st.xy));
	vec3 color = vec3(0.325,0.740,0.980);
    
	// color	    
    vec3 final_color = color*vec3(mask.x,mask.x,mask);
    final_color.r = st.x;
    fragColor = vec4(final_color, 1.);
}
```
