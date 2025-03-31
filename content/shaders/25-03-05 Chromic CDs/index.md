---
title: Chromic CDs
date: 2025-03-05
rank: 0
summary: chromic cds
description: chromic cds
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
<iframe width="700" height="700" frameborder="0" src="https://www.shadertoy.com/embed/WfXXzl?gui=true&t=0&paused=false&muted=false" allowfullscreen></iframe>

learning gradient, circle, grid, masking, noise / random

View on [**ShaderToy**](https://www.shadertoy.com/view/WfXXzl)

```glsl
// Author: Baangkok Vanijyananda
// Title: Chromic CDs

#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359
#define PHI 1.61803398874989484820459  // Φ = Golden Ratio   
#define RANDOM_SEED 987653.0

const vec3 col_black = vec3(2, 2, 2)/255.;
const vec3 col_blue_dark = vec3(24, 29, 45)/255.;
const vec3 col_blue_middle = vec3(92, 128, 146)/255.;
const vec3 col_white = vec3(228, 232, 231)/255.;

float gold_noise(in vec2 xy, in float seed){
       return fract(tan(distance(xy*PHI, xy)*seed)*xy.x);
}

vec2 rotateUV(vec2 uv, float rotation, vec2 mid)
{
    return vec2(
      cos(rotation) * (uv.x - mid.x) + sin(rotation) * (uv.y - mid.y) + mid.x,
      cos(rotation) * (uv.y - mid.y) - sin(rotation) * (uv.x - mid.x) + mid.y
    );
}

vec3 get_gradient_color(float gradient_direction) {
    vec3 pct = vec3(smoothstep(0.8, 1.,gradient_direction));
    vec3 pct2 = vec3(smoothstep(0.5, 0.9,gradient_direction));
    vec3 pct3 = vec3(smoothstep(0.0, 0.7,gradient_direction));

    vec3 color = vec3(1.);
    color = mix(col_blue_dark, col_black, pct);
    color = mix(col_blue_middle, color, pct2);
    color = mix(col_white, color, pct3);
    return color;
}

// xy is normalized, unrepeated coord
float mask_grid(vec2 xy, float seed, float grid_size, float threshold){
    vec2 grid_bottom_left = xy-mod(xy, 1./grid_size)+(1./grid_size)*0.5;
    float mask = step(threshold, gold_noise(grid_bottom_left, seed));
    return mask;
}

float mask_circle(vec2 uv, float radius_outer, float border_thickness, vec2 position){
    
    /// inner circle
    float radius_inner = radius_outer - border_thickness;
    float d_inner = sqrt(dot(uv-position,uv-position));
    float t_inner = 1.0 - smoothstep(radius_inner,radius_inner, d_inner);
    
    /// outer circle
    float d_outer = sqrt(dot(uv-position,uv-position));
    float t_outer = 1.0 - smoothstep(radius_outer,radius_outer, d_outer);
    
    /// mask
	return t_outer - t_inner;
}


void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
        vec2 uv = fragCoord.xy/iResolution.xy;
    uv.x *= iResolution.x/iResolution.y;
    vec2 unrepeated_uv = uv;
    
    // repeat coordinate
    float repeat_count = 4.;
	float spacing = 1./repeat_count;
    float repeat_offset = 0.;
    
    uv.x = mod(uv.x+repeat_offset, spacing)/spacing;
    uv.y = mod(uv.y+repeat_offset, spacing)/spacing;
    
    // gradient
    vec2 bg_uv = rotateUV(uv, 1.8*PI, vec2(0.5,0.5));
    vec3 gradient_color = get_gradient_color(bg_uv.y);
    
    vec2 rotated_uv = rotateUV(uv, iTime, vec2(0.5,0.5));
    vec3 rotated_gradient_color = get_gradient_color(rotated_uv.y);
    
    // circle
    float circle_mask = mask_circle(rotated_uv, 0.5, 0.08, vec2(0.5,0.5));
    float circle_mask_thick = mask_circle(rotated_uv, 0.5, 0.248, vec2(0.5,0.5));

    // mask grid randomized
    float mask_grid_randomized = mask_grid(unrepeated_uv, RANDOM_SEED,repeat_count,0.372);
    float mask_grid_randomized_2 = mask_grid(unrepeated_uv, RANDOM_SEED+-0.168,repeat_count,0.796);
    float circle_mask_grid = mix(0., circle_mask, mask_grid_randomized);
    float circle_thick_mask_grid = mix(0., circle_mask_thick, mask_grid_randomized_2);
    
    vec3 color = gradient_color;
    color = mix(color, rotated_gradient_color*1.2, circle_mask_grid);
    color = mix(color, rotated_gradient_color*1.2, circle_thick_mask_grid);


    // noise
    float noise = gold_noise(uv.xy+1., RANDOM_SEED);
    color = mix(color, vec3(noise), 0.060);
    
    // final color
	vec3 final_color = color;

    fragColor = vec4(color,1.0);
}
```
