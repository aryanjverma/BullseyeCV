# 🎯 BullseyeCV

**BullseyeCV** is a computer vision system that automatically detects arrow impact locations and computes scores from archery target video streams. The system is designed to work under real-world conditions including camera motion, perspective distortion, and arrow overlap by leveraging geometric reasoning and direction-aware inference.

---

## 🚀 Motivation

Most automated archery scoring solutions rely on ideal assumptions:
- Fixed, perfectly aligned cameras
- No arrow overlap
- Clearly visible arrow tips

In practice, cameras move, arrows overlap, and the visible tip is not always the true scoring point.  
BullseyeCV addresses these challenges using **homography normalization**, **temporal image differencing**, and **arrow direction estimation** to robustly infer true impact locations.

---

## ✨ Key Features

### 📐 Target Normalization
- Detects the target paper by identifying the largest square contour
- Applies a homographic transformation to map the target into a canonical coordinate space
- Eliminates camera translation, rotation, and perspective distortion

### 🏹 Arrow Impact Detection
- Uses frame differencing to isolate newly embedded arrows
- Extracts arrow contours even under partial occlusion
- Operates on live video streams

### 🧭 Direction-Aware Scoring
- Estimates arrow orientation using contour geometry and principal-axis analysis
- Infers the **true arrow tip** by extrapolating along the arrow’s direction vector
- Correctly scores arrows when overlap hides the visible tip

### 🎯 Multi-Format Target Support
- Supports multiple archery formats (e.g. Vegas 1-Spot, Vegas 3-Spot, NFAA)
- Parameterizes ring geometry, scale calibration, and center locations
- Enables vectorized score computation

---

## 🛠️ Core Technologies

- **Python**
- **OpenCV**
- Homography & perspective correction
- Contour analysis
- PCA / principal axis estimation
- Geometric extrapolation
- Temporal image differencing

---

## 📷 Example Workflow

1. Client streams target video using OBS
2. Stream is ingested via YouTube Live or RTMP relay
3. BullseyeCV detects and normalizes the target region
4. New arrow impacts are detected between frames
5. Arrow direction is estimated to infer the true impact point
6. Impact point is mapped to target rings for scoring

---

## 🔮 Future Improvements

- ML-based arrow segmentation for higher robustness
- Automatic direction learning without prior assumptions
- Multi-camera fusion for depth-aware scoring
- Real-time score overlays
- Expanded target format support

---

## 🧪 Why BullseyeCV?

BullseyeCV demonstrates how **classical computer vision and geometry** can solve a physically grounded problem more reliably than naïve heuristics. The project emphasizes robustness, interpretability, and real-world deployment over idealized lab conditions.

---

## 👤 Author

**Aryan Verma**  
Computer Science — The University of Texas at Austin  
Interests: Computer Vision, AI, Math
