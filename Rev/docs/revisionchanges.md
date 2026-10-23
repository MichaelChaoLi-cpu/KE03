# Manuscript Revision Changes

Schema: `kila-revision-changes/v1`

## reviewer-2/comment-4

### part-01

- Location: Introduction / Research Questions and Contributions
- Reason: 删除无依据的独立性属性；保留四贡献段的结构，明确 terrain/channel 是物理语境。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:19:27Z
- Author: Mike Li
- Markup SHA-256 before: `951be11f859b243f9c94896769bf0d8246b9f7e62a6cd578c3a0f2f0fc496d64`
- Markup SHA-256 after: `237acf37c711fe36060d80f19d168afa2384c2aeeb96a8042c6234e738b9b3d9`
- Revision IDs: `1, 2, 3, 4, 5, 6, 7, 8, 9`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T141927979262.reviewer-2-comment-4.part-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
First, independent mapped, sensor, terrain, and channel evidence form nested hazard-confidence footprints.
~~~~

- After:

~~~~text
First, mapped and sensor evidence, with terrain and channel context, form nested hazard-confidence footprints.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "independent"
     - After: "mapped"
  2. `replace`
     - Before: "mapped"
     - After: "and sensor evidence"
  3. `replace`
     - Before: "sensor,"
     - After: "with"
  4. `delete`
     - Before: ","
     - After: ""
  5. `replace`
     - Before: "evidence"
     - After: "context,"

### part-02

- Location: Study Area and Data / Hazard and Geospatial Evidence / first paragraph
- Reason: 补齐产品编号、实际版本、影像日期与制图方法；明确 UNOSAT 与研究光学输入同日。保留阈值、20 m 网格、地形/河道参数及 Novelli 引用。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:38Z
- Author: Mike Li
- Markup SHA-256 before: `237acf37c711fe36060d80f19d168afa2384c2aeeb96a8042c6234e738b9b3d9`
- Markup SHA-256 after: `0030d90a0824585ee831847643b084947d3ac81f670023f00bc7e8bc068207d8`
- Revision IDs: `10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144339114833.reviewer-2-comment-4.part-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The study team assembled the reconstruction from UNOSAT reference mapping; three areas of interest from the European Union's Copernicus Emergency Management Service; Sentinel-1 observations from 16 and 28 August 2026 and cloud- and snow-masked Sentinel-2 imagery distributed through Microsoft Planetary Computer; the Copernicus DEM; HydroSHEDS rivers; RGI Consortium glacier outlines; and Nepal administrative boundaries distributed by OCHA and HDX. Radar provides spatially complete evidence of change within the event window, while the optical observations add support where both dates contain valid pixels. The primary radar screen identifies a post-minus-pre VH decrease of at least 2 dB, and the optical screen identifies a post-minus-pre MNDWI increase of at least 0.15. Terrain context uses slopes of at least 30° and channel context uses a 120 m buffer around the mapped drainage network. Independent UNOSAT and Copernicus extents provide reference evidence against which the sensor screens are compared. Integrated satellite and field investigations in other disasters demonstrate the value of combining complementary observation modes rather than relying on a single change product (Novelli et al., 2026). The aligned project layers use a 20 m grid and consistent Sentinel-1 acquisition geometry. Their agreement defines nested evidence-confidence classes for subsequent exposure and network scenarios.
~~~~

- After:

~~~~text
The reconstruction uses UNOSAT products 4257 and 4258 (FL20260826NPL), three AOIs from CEMS activation EMSR927, Sentinel-1 and Sentinel-2 imagery from Microsoft Planetary Computer, the Copernicus DEM, HydroSHEDS rivers, RGI glacier outlines, and OCHA/HDX administrative boundaries. UNOSAT delineates mudflow and rockflow from PlanetScope imagery acquired on 26 August 2026 and Sentinel-2 imagery acquired on 27 August 2026. The selected CEMS products are AOI01 GRA PRODUCT v1, AOI02 GRA PRODUCT v2, and AOI03 GRA MONIT01 v1; they use visual interpretation of WorldView-3 and Legion imagery from 27 August 2026 and PeruSAT-1 and Resurs-P imagery from 27 and 28 August 2026, respectively. Our radar and optical comparisons use Sentinel-1 acquisitions from 16 and 28 August 2026 and Sentinel-2 acquisitions from 12 and 27 August 2026, respectively. The primary screens identify a VH decrease of at least 2 dB and an MNDWI increase of at least 0.15; terrain and channel context use slopes of at least 30° and a 120 m drainage buffer. UNOSAT and our optical input share the Sentinel-2 acquisition date, so their agreement is interpreted as source convergence. Integrated satellite and field investigations in other disasters demonstrate the value of combining complementary observation modes rather than relying on a single change product (Novelli et al., 2026). The aligned project layers use a 20 m grid and consistent Sentinel-1 acquisition geometry. Their agreement defines nested evidence-confidence classes for subsequent exposure and network scenarios.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "study"
     - After: "reconstruction"
  2. `replace`
     - Before: "team"
     - After: "uses"
  3. `replace`
     - Before: "assembled"
     - After: "UNOSAT products 4257 and 4258 (FL20260826NPL), three AOIs from CEMS activation EMSR927, Sentinel-1 and Sentinel-2 imagery from Microsoft Planetary Computer,"
  4. `replace`
     - Before: "reconstruction"
     - After: "Copernicus DEM, HydroSHEDS rivers, RGI glacier outlines, and OCHA/HDX administrative boundaries. UNOSAT delineates mudflow and rockflow"
  5. `replace`
     - Before: "UNOSAT"
     - After: "PlanetScope"
  6. `replace`
     - Before: "reference"
     - After: "imagery"
  7. `replace`
     - Before: "mapping"
     - After: "acquired on 26 August 2026 and Sentinel-2 imagery acquired on 27 August 2026. The selected CEMS products are AOI01 GRA PRODUCT v1, AOI02 GRA PRODUCT v2, and AOI03 GRA MONIT01 v1"
  8. `replace`
     - Before: "three"
     - After: "they"
  9. `replace`
     - Before: "areas"
     - After: "use visual interpretation"
  10. `replace`
     - Before: "interest"
     - After: "WorldView-3 and Legion imagery"
  11. `replace`
     - Before: "the"
     - After: "27"
  12. `replace`
     - Before: "European"
     - After: "August"
  13. `replace`
     - Before: "Union's"
     - After: "2026"
  14. `replace`
     - Before: "Copernicus"
     - After: "and"
  15. `replace`
     - Before: "Emergency"
     - After: "PeruSAT-1"
  16. `replace`
     - Before: "Management"
     - After: "and"
  17. `replace`
     - Before: "Service;"
     - After: "Resurs-P imagery from 27 and 28 August 2026, respectively. Our radar and optical comparisons use"
  18. `replace`
     - Before: "observations"
     - After: "acquisitions"
  19. `replace`
     - Before: "cloud-"
     - After: "Sentinel-2 acquisitions from 12"
  20. `replace`
     - Before: "snow-masked"
     - After: "27"
  21. `replace`
     - Before: "Sentinel-2"
     - After: "August"
  22. `replace`
     - Before: "imagery"
     - After: "2026"
  23. `delete`
     - Before: " distributed through Microsoft Planetary Computer; the Copernicus DEM; HydroSHEDS rivers; RGI Consortium glacier outlines; and Nepal administrative boundaries distributed by OCHA and HDX. Radar provides spatially complete evidence of change within the event window"
     - After: ""
  24. `replace`
     - Before: "while the optical observations add support where both dates contain valid pixels"
     - After: "respectively"
  25. `replace`
     - Before: "radar"
     - After: "screens"
  26. `replace`
     - Before: "screen identifies"
     - After: "identify"
  27. `delete`
     - Before: " post-minus-pre"
     - After: ""
  28. `delete`
     - Before: ","
     - After: ""
  29. `replace`
     - Before: "the optical screen identifies a post-minus-pre"
     - After: "an"
  30. `replace`
     - Before: "."
     - After: ";"
  31. `replace`
     - Before: "Terrain"
     - After: "terrain and channel"
  32. `replace`
     - Before: "uses"
     - After: "use"
  33. `delete`
     - Before: "channel context uses "
     - After: ""
  34. `delete`
     - Before: "buffer around the mapped "
     - After: ""
  35. `replace`
     - Before: "network"
     - After: "buffer"
  36. `delete`
     - Before: " Independent"
     - After: ""
  37. `replace`
     - Before: "Copernicus"
     - After: "our"
  38. `replace`
     - Before: "extents"
     - After: "optical"
  39. `replace`
     - Before: "provide"
     - After: "input"
  40. `replace`
     - Before: "reference evidence against which"
     - After: "share"
  41. `replace`
     - Before: "sensor"
     - After: "Sentinel-2"
  42. `replace`
     - Before: "screens"
     - After: "acquisition"
  43. `replace`
     - Before: "are"
     - After: "date,"
  44. `replace`
     - Before: "compared"
     - After: "so their agreement is interpreted as source convergence"

### part-03

- Location: Study Area and Data / Hazard and Geospatial Evidence / second paragraph
- Reason: 移除未经证明的独立性，并准确对应现有 class-3 OR 规则；分类算法和数值不变。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:39Z
- Author: Mike Li
- Markup SHA-256 before: `0030d90a0824585ee831847643b084947d3ac81f670023f00bc7e8bc068207d8`
- Markup SHA-256 after: `79d00e2911aa6f12bf050fa5676e6c6d43ac278a95bb2370675ae0416fca2236`
- Revision IDs: `92, 93, 94, 95, 96, 97, 98, 99, 100, 101`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144339816646.reviewer-2-comment-4.part-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The conservative footprint requires convergence among independent mapped and sensor sources, while broader classes retain areas with fewer supporting sources.
~~~~

- After:

~~~~text
The conservative footprint requires agreement between both mapped products or between at least one mapped product and one sensor signal, while broader classes retain areas with fewer supporting sources.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "convergence"
     - After: "agreement"
  2. `replace`
     - Before: "among"
     - After: "between"
  3. `replace`
     - Before: "independent"
     - After: "both"
  4. `insert`
     - Before: ""
     - After: "products or between at least one mapped product "
  5. `insert`
     - Before: ""
     - After: " one"
  6. `replace`
     - Before: "sources"
     - After: "signal"

### part-04

- Location: Methodology / Cascading-Hazard Evidence Reconstruction
- Reason: 方法定义与数据说明一致，既有分类定义的精细敏感性问题留给 reviewer-4/comment-1，不在本条擅改算法。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:40Z
- Author: Mike Li
- Markup SHA-256 before: `79d00e2911aa6f12bf050fa5676e6c6d43ac278a95bb2370675ae0416fca2236`
- Markup SHA-256 after: `61f9a08a0fbe8c606fc85b51fc56c9fb163b0ac172916532044b3912734414dd`
- Revision IDs: `102, 103, 104, 105, 106, 107, 108, 109, 110, 111`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144340538984.reviewer-2-comment-4.part-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The conservative class requires convergence among independent mapped and sensor evidence; the alternative class admits mapped or multisensor support; and the broad sensitivity class includes any positive event evidence.
~~~~

- After:

~~~~text
The conservative class requires agreement between both mapped products or between at least one mapped product and one sensor signal; the alternative class admits mapped or multisensor support; and the broad sensitivity class includes any positive event evidence.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "convergence"
     - After: "agreement"
  2. `replace`
     - Before: "among"
     - After: "between"
  3. `replace`
     - Before: "independent"
     - After: "both"
  4. `insert`
     - Before: ""
     - After: "products or between at least one mapped product "
  5. `insert`
     - Before: ""
     - After: " one"
  6. `replace`
     - Before: "evidence"
     - After: "signal"

### part-05

- Location: Results / section heading
- Reason: 按 reviewer 要求纠正当前证据角色；不把地图间一致性称作独立验证。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:41Z
- Author: Mike Li
- Markup SHA-256 before: `61f9a08a0fbe8c606fc85b51fc56c9fb163b0ac172916532044b3912734414dd`
- Markup SHA-256 after: `6d765cab5dc47e2cf1fb7304657340045a4d97e497a81a61491bb89bd72a4002`
- Revision IDs: `112, 113`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144341253044.reviewer-2-comment-4.part-05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Evidence Validation and Hazard Footprint
~~~~

- After:

~~~~text
Evidence Agreement and Hazard Footprint
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Validation"
     - After: "Agreement"

### part-06

- Location: Results / Evidence Agreement and Hazard Footprint / first paragraph
- Reason: 删除独立 reference mapping 的无依据属性，保留原有核心/宽类别叙述。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:52Z
- Author: Mike Li
- Markup SHA-256 before: `6d765cab5dc47e2cf1fb7304657340045a4d97e497a81a61491bb89bd72a4002`
- Markup SHA-256 after: `650e57873001c5b88c081dcbe47b722ca68c3806e8e9f7f3c31a234757ea3bf1`
- Revision IDs: `114, 115, 116, 117, 118, 119, 120, 121`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144352289929.reviewer-2-comment-4.part-06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Agreement between independent reference mapping and sensor change defines the conservative core; locations supported by fewer sources remain within broader evidence classes.
~~~~

- After:

~~~~text
Agreement between mapped products, or between mapped and sensor evidence, defines the conservative core; locations supported by fewer sources remain within broader evidence classes.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "independent"
     - After: "mapped"
  2. `replace`
     - Before: "reference"
     - After: "products,"
  3. `replace`
     - Before: "mapping"
     - After: "or between mapped"
  4. `replace`
     - Before: "change"
     - After: "evidence,"

### part-07

- Location: Results / Evidence Agreement and Hazard Footprint / second paragraph / radar comparison
- Reason: 保留 29.6% 与 9.4% 的已报告对比，仅把其解释限定为已计算的一致性，不用这些比例推断独立准确率或未标注像素真实错误。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:52Z
- Author: Mike Li
- Markup SHA-256 before: `650e57873001c5b88c081dcbe47b722ca68c3806e8e9f7f3c31a234757ea3bf1`
- Markup SHA-256 after: `fd30755186225c6c0d4fda5e25e6725e898d0cee58bc94f4640b89d26f350471`
- Revision IDs: `122, 123, 124, 125, 126, 127, 128, 129, 130, 131`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144353003468.reviewer-2-comment-4.part-07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
This contrast supports the radar signal as a screening layer while showing that its threshold alone would include many unrelated changes.
~~~~

- After:

~~~~text
This contrast quantifies spatial agreement between the radar screen and UNOSAT mapping.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "supports"
     - After: "quantifies spatial agreement between"
  2. `replace`
     - Before: "signal"
     - After: "screen"
  3. `replace`
     - Before: "as"
     - After: "and"
  4. `replace`
     - Before: "a"
     - After: "UNOSAT"
  5. `replace`
     - Before: "screening layer while showing that its threshold alone would include many unrelated changes"
     - After: "mapping"

### part-08

- Location: Results / Evidence Agreement and Hazard Footprint / second paragraph / confidence classes
- Reason: 与现有 class-3 计算规则和方法措辞一致，取消独立性暗示。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:53Z
- Author: Mike Li
- Markup SHA-256 before: `fd30755186225c6c0d4fda5e25e6725e898d0cee58bc94f4640b89d26f350471`
- Markup SHA-256 after: `028d253765734dc197679aaf9fee745c96d4b3662a7d7dfe8733d42b8209829b`
- Revision IDs: `132, 133, 134, 135, 136, 137`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144353791497.reviewer-2-comment-4.part-08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The conservative class selects areas where independent mapped and sensor sources converge; classes 2 and 1 progressively admit evidence with fewer supporting sources.
~~~~

- After:

~~~~text
The conservative class selects areas with agreement between mapped products or between mapped and sensor evidence; classes 2 and 1 progressively admit evidence with fewer supporting sources.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "where"
     - After: "with"
  2. `replace`
     - Before: "independent"
     - After: "agreement between mapped products or between"
  3. `replace`
     - Before: "sources converge"
     - After: "evidence"

### part-09

- Location: Figures / Figure 1 explanatory note
- Reason: 图注直接说明来源关系；只改说明文字，不替换 PNG 或绘图对象。
- Kila decisions: KILA-D-20261023-002
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T05:43:54Z
- Author: Mike Li
- Markup SHA-256 before: `028d253765734dc197679aaf9fee745c96d4b3662a7d7dfe8733d42b8209829b`
- Markup SHA-256 after: `2cf7c82cea5e2648b2205c8d932c661c00abd09c6e8d752f4482c7431b3fcc52`
- Revision IDs: `138, 139`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T144354515528.reviewer-2-comment-4.part-09.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Panel c compares agreement between mapped and sensor evidence.
~~~~

- After:

~~~~text
Panel c compares mapped and sensor evidence; the UNOSAT and study optical inputs share a Sentinel-2 acquisition date.
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " agreement between"
     - After: ""
  2. `insert`
     - Before: ""
     - After: "; the UNOSAT and study optical inputs share a Sentinel-2 acquisition date"

## reviewer-4/comment-2

### part-01

- Location: Study Area and Data / Settlements, Roads, Services, and Population
- Reason: 补齐等级来源、投影、道路/桥梁匹配方向和容差及源要素覆盖；不将足迹相交自行视为Destroyed。
- Kila decisions: KILA-D-20261023-004
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T06:28:43Z
- Author: Mike Li
- Markup SHA-256 before: `2cf7c82cea5e2648b2205c8d932c661c00abd09c6e8d752f4482c7431b3fcc52`
- Markup SHA-256 after: `ac2db10ce5a1f64d33443f3acb5188b8074d95399160fe2dbbd31fbfcd885044`
- Revision IDs: `140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T152843239742.reviewer-4-comment-2.part-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Bridges and facility intersections are also recorded to identify locations where operating status is relevant to interpretation.
~~~~

- After:

~~~~text
CEMS EMSR927 grades are linked to OSM edges in EPSG:32645 using 20 m buffers around road lines and, for OSM-tagged bridge edges, the nearest CEMS bridge point within 100 m; 700 of 706 road features and 18 of 32 bridge points match the graph.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Bridges"
     - After: "CEMS EMSR927 grades are linked to OSM edges in EPSG:32645 using 20 m buffers around road lines and, for OSM-tagged bridge edges, the nearest CEMS bridge point within 100 m; 700 of 706 road features"
  2. `replace`
     - Before: "facility"
     - After: "18"
  3. `replace`
     - Before: "intersections"
     - After: "of"
  4. `replace`
     - Before: "are"
     - After: "32"
  5. `replace`
     - Before: "also"
     - After: "bridge"
  6. `replace`
     - Before: "recorded"
     - After: "points"
  7. `replace`
     - Before: "to"
     - After: "match"
  8. `replace`
     - Before: "identify"
     - After: "the"
  9. `replace`
     - Before: "locations"
     - After: "graph"
  10. `delete`
     - Before: " where operating status is relevant to interpretation"
     - After: ""

### part-02

- Location: Methodology / Network Disruption and Service Accessibility
- Reason: 明确三个同时成立的闭路条件、最重等级、两套规则及部分相交仍关闭整边的处理。保留全部周边速度与访问定义。
- Kila decisions: KILA-D-20261023-004
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T06:28:55Z
- Author: Mike Li
- Markup SHA-256 before: `ac2db10ce5a1f64d33443f3acb5188b8074d95399160fe2dbbd31fbfcd885044`
- Markup SHA-256 after: `15d74012cee47def0616e5ba9d14a63c8388a9b5c99720f8a9e24604161fe403`
- Revision IDs: `159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T152855911186.reviewer-4-comment-2.part-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
A disruption scenario removes edges that satisfy its closure rule within the selected hazard footprint and then recalculates all shortest paths.
~~~~

- After:

~~~~text
For each scenario, an edge is removed only if it belongs to the selected topology-specific graph, intersects a raster cell meeting the hazard-class threshold under all-touched rasterization, and has a qualifying CEMS grade, taking the most severe grade when several features match. The primary rule admits Destroyed, while the broader rule also admits Possibly damaged and Damaged. Qualifying conditions close the entire edge before shortest paths are recalculated, even when only part intersects the selected footprint.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "A"
     - After: "For"
  2. `replace`
     - Before: "disruption"
     - After: "each"
  3. `insert`
     - Before: ""
     - After: ","
  4. `replace`
     - Before: "removes"
     - After: "an"
  5. `replace`
     - Before: "edges"
     - After: "edge"
  6. `replace`
     - Before: "that"
     - After: "is"
  7. `replace`
     - Before: "satisfy"
     - After: "removed"
  8. `replace`
     - Before: "its"
     - After: "only"
  9. `replace`
     - Before: "closure"
     - After: "if"
  10. `replace`
     - Before: "rule"
     - After: "it"
  11. `replace`
     - Before: "within"
     - After: "belongs to"
  12. `replace`
     - Before: "hazard"
     - After: "topology-specific"
  13. `replace`
     - Before: "footprint"
     - After: "graph, intersects a raster cell meeting the hazard-class threshold under all-touched rasterization,"
  14. `replace`
     - Before: "then"
     - After: "has"
  15. `replace`
     - Before: "recalculates"
     - After: "a"
  16. `replace`
     - Before: "all"
     - After: "qualifying CEMS grade, taking the most severe grade when several features match. The primary rule admits Destroyed, while the broader rule also admits Possibly damaged and Damaged. Qualifying conditions close the entire edge before"
  17. `insert`
     - Before: ""
     - After: " are recalculated, even when only part intersects the selected footprint"

### part-03

- Location: Results / Network Disruption and Service-Access Loss / first paragraph
- Reason: 增加新审计已验证的图边数量、完整边长度和部分相交数量；不改人口、可达性或恢复效益数值。
- Kila decisions: KILA-D-20261023-004
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T06:29:13Z
- Author: Mike Li
- Markup SHA-256 before: `15d74012cee47def0616e5ba9d14a63c8388a9b5c99720f8a9e24604161fe403`
- Markup SHA-256 after: `a264e74bb06451eed2920c96e99d980fc91a3e5bf7a246057cdc928b0a329b9b`
- Revision IDs: `191, 192, 193, 194, 195, 196, 197, 198`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T152913530244.reviewer-4-comment-2.part-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Figure 2 connects the primary closed edges with baseline access and post-disruption status.
~~~~

- After:

~~~~text
Figure 2 maps the 2,023 primary-closed graph edges (54.79 km), of which 199 intersect the class-3 footprint only partially, alongside baseline access and post-disruption status.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "connects"
     - After: "maps"
  2. `replace`
     - Before: "primary"
     - After: "2,023"
  3. `replace`
     - Before: "closed"
     - After: "primary-closed graph"
  4. `replace`
     - Before: "with"
     - After: "(54.79 km), of which 199 intersect the class-3 footprint only partially, alongside"

### part-04

- Location: Figures / Figure 2 explanatory note
- Reason: 在图注中直接说明Destroyed等级、class-3足迹与完整图边；只改文字，不替换图像。
- Kila decisions: KILA-D-20261023-004
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T06:29:22Z
- Author: Mike Li
- Markup SHA-256 before: `a264e74bb06451eed2920c96e99d980fc91a3e5bf7a246057cdc928b0a329b9b`
- Markup SHA-256 after: `d8cd84625b2276f3d4cec62f886bc419306a0160d54911bddeebc80dec567d7a`
- Revision IDs: `199, 200, 201, 202, 203, 204, 205, 206`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T152922589566.reviewer-4-comment-2.part-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Panel a maps evidence-linked primary road closures.
~~~~

- After:

~~~~text
Panel a maps full graph edges selected for modeled closure by both CEMS Destroyed grades and class-3 footprint intersection.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "evidence-linked"
     - After: "full"
  2. `replace`
     - Before: "primary"
     - After: "graph"
  3. `replace`
     - Before: "road"
     - After: "edges"
  4. `replace`
     - Before: "closures"
     - After: "selected for modeled closure by both CEMS Destroyed grades and class-3 footprint intersection"

## reviewer-4/comment-3

### part-01

- Location: Study Area and Data / Settlements, Roads, Services, and Population / population paragraph
- Reason: 明确最近对象、同一行政单元、栅格中心和米制距离。
- Kila decisions: KILA-D-20261023-006
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:19:05Z
- Author: Mike Li
- Markup SHA-256 before: `d8cd84625b2276f3d4cec62f886bc419306a0160d54911bddeebc80dec567d7a`
- Markup SHA-256 after: `58c84118664c74f9e4af6d4f41aa522a311cfbc69794f563cc525a28e4cc713d`
- Revision IDs: `207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T161905349299.reviewer-4-comment-3.part-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Grid-cell counts are assigned to mapped settlements within each local unit using pre-specified distance thresholds.
~~~~

- After:

~~~~text
Grid-cell counts are assigned to the nearest mapped settlement in the same local unit, using cell-center distances in EPSG:32645 and a primary limit of 3 km.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "the nearest "
  2. `replace`
     - Before: "settlements"
     - After: "settlement"
  3. `replace`
     - Before: "within"
     - After: "in"
  4. `replace`
     - Before: "each"
     - After: "the same"
  5. `insert`
     - Before: ""
     - After: ","
  6. `replace`
     - Before: "pre-specified"
     - After: "cell-center"
  7. `replace`
     - Before: "distance"
     - After: "distances"
  8. `replace`
     - Before: "thresholds"
     - After: "in EPSG:32645 and a primary limit of 3 km"

### part-02

- Location: Methodology / Exposure and Population Allocation / population-allocation paragraph
- Reason: 补充栅格行政归属、单对象、重叠不重复、实测无并列、未分配原因和独立守恒；明确阈值只筛选固定最近记录。
- Kila decisions: KILA-D-20261023-006
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:19:21Z
- Author: Mike Li
- Markup SHA-256 before: `58c84118664c74f9e4af6d4f41aa522a311cfbc69794f563cc525a28e4cc713d`
- Markup SHA-256 after: `c8837a3068ddf3404cccaf67f621c47593aba353770bf4506f265d56d0640ac7`
- Revision IDs: `221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T161921337090.reviewer-4-comment-3.part-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
We estimate settlement population by assigning calibrated grid values to mapped settlements within pre-specified distance thresholds. The primary allocation uses the widest confirmed threshold, while three narrower alternatives progressively reduce the represented population.
~~~~

- After:

~~~~text
Local-unit membership follows cell-center rasterization of the administrative polygons. Each positive-population cell has one nearest-settlement record, so overlapping distance buffers do not duplicate counts; no exact nearest-distance ties occur among the 228,289 cells. Cells beyond the threshold or in units without mapped settlements remain unallocated, and assigned plus unallocated population equals the raster total within every local unit and across the study area. The primary threshold is 3 km, with 500 m, 1 km, and 2 km alternatives evaluated against the same nearest-settlement records.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "We"
     - After: "Local-unit"
  2. `replace`
     - Before: "estimate"
     - After: "membership"
  3. `replace`
     - Before: "settlement"
     - After: "follows"
  4. `replace`
     - Before: "population"
     - After: "cell-center"
  5. `replace`
     - Before: "by"
     - After: "rasterization"
  6. `replace`
     - Before: "assigning"
     - After: "of"
  7. `replace`
     - Before: "calibrated"
     - After: "the"
  8. `replace`
     - Before: "grid"
     - After: "administrative"
  9. `replace`
     - Before: "values"
     - After: "polygons."
  10. `replace`
     - Before: "to"
     - After: "Each positive-population cell has one nearest-settlement record, so overlapping distance buffers do not duplicate counts; no exact nearest-distance ties occur among the 228,289 cells. Cells beyond the threshold or in units without"
  11. `insert`
     - Before: ""
     - After: "remain unallocated, and assigned plus unallocated population equals the raster total "
  12. `replace`
     - Before: "pre-specified"
     - After: "every"
  13. `replace`
     - Before: "distance"
     - After: "local"
  14. `replace`
     - Before: "thresholds"
     - After: "unit and across the study area"
  15. `replace`
     - Before: "allocation"
     - After: "threshold"
  16. `replace`
     - Before: "uses"
     - After: "is 3 km, with 500 m, 1 km, and 2 km alternatives evaluated against"
  17. `replace`
     - Before: "widest"
     - After: "same"
  18. `replace`
     - Before: "confirmed"
     - After: "nearest-settlement"
  19. `replace`
     - Before: "threshold, while three narrower alternatives progressively reduce the represented population"
     - After: "records"

### part-03

- Location: Results / Network Disruption and Service-Access Loss / first paragraph, opening sentence
- Reason: 在原开头前补互斥的已分配人口路网覆盖分解，避免90.2%被误读为访问分析覆盖率；完整保留原开头及上条Figure2修订。
- Kila decisions: KILA-D-20261023-006
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:19:31Z
- Author: Mike Li
- Markup SHA-256 before: `c8837a3068ddf3404cccaf67f621c47593aba353770bf4506f265d56d0640ac7`
- Markup SHA-256 after: `deee02e89f0040218bfec0c4ef4426648660552ac928fbc8d5ba0a44ba8195b0`
- Revision IDs: `258`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T161931511103.reviewer-4-comment-3.part-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Evidence-linked closures produce finite delays near the southern corridor and a longer chain of newly isolated settlements toward the north.
~~~~

- After:

~~~~text
Of the 573,645 assigned people, 532,382 belong to the 610 baseline-eligible settlements, 36,182 to 110 baseline-unreachable settlements within the road-snap limit, and 5,081 to 47 settlements beyond that limit. Evidence-linked closures produce finite delays near the southern corridor and a longer chain of newly isolated settlements toward the north.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "Of the 573,645 assigned people, 532,382 belong to the 610 baseline-eligible settlements, 36,182 to 110 baseline-unreachable settlements within the road-snap limit, and 5,081 to 47 settlements beyond that limit. "

### part-04

- Location: Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 给出四阈值覆盖、入组与top-ten成员变化的实际结果，把75%转为可读的三次/四次；不改主排序。
- Kila decisions: KILA-D-20261023-006
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:19:42Z
- Author: Mike Li
- Markup SHA-256 before: `deee02e89f0040218bfec0c4ef4426648660552ac928fbc8d5ba0a44ba8195b0`
- Markup SHA-256 after: `2a7c2770e372c88b59891ceb6c787cb52b0c83fa67f727a876f54725a11982e6`
- Revision IDs: `259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T161942331045.reviewer-4-comment-3.part-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Allocation persistence falls to 75% for Rasuwa Gadhi, Gerkhu, and the tenth-ranked unnamed settlement.
~~~~

- After:

~~~~text
Across the 500 m, 1 km, 2 km, and 3 km allocations, population coverage is 27.5%, 47.6%, 76.1%, and 90.2%, and ranking eligibility comprises 82, 82, 83, and 84 settlements. The 500 m allocation retains seven primary top-ten members, while the other thresholds retain all ten; Rasuwa Gadhi, Gerkhu, and the tenth-ranked unnamed settlement each persist in three of four allocations.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Allocation"
     - After: "Across"
  2. `replace`
     - Before: "persistence"
     - After: "the"
  3. `replace`
     - Before: "falls"
     - After: "500"
  4. `replace`
     - Before: "to"
     - After: "m,"
  5. `replace`
     - Before: "75"
     - After: "1 km, 2 km, and 3 km allocations, population coverage is 27.5"
  6. `insert`
     - Before: ""
     - After: ","
  7. `replace`
     - Before: "for"
     - After: "47.6%, 76.1%, and 90.2%, and ranking eligibility comprises 82, 82, 83, and 84 settlements. The 500 m allocation retains seven primary top-ten members, while the other thresholds retain all ten;"
  8. `insert`
     - Before: ""
     - After: " each persist in three of four allocations"

### part-05

- Location: Discussion / Limitations and Future Validation / paragraph beginning Several limitations
- Reason: 披露边界约束的实测覆盖后果，纠正阈值改变会重分配既有栅格的含混说法；用正向范围说明替代防御性句子。
- Kila decisions: KILA-D-20261023-006
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:19:54Z
- Author: Mike Li
- Markup SHA-256 before: `2a7c2770e372c88b59891ceb6c787cb52b0c83fa67f727a876f54725a11982e6`
- Markup SHA-256 after: `d9b93892c1514067d88bfc187cd852caaf04e1f266e9bf57b24c1abf17c1a96d`
- Revision IDs: `273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289`
- Backup: `Rev/revision/.kila-backups/KE03.rev.markup.20261023T161955092020.reviewer-4-comment-3.part-05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Population allocation excludes people beyond the selected distance and may redistribute represented population among nearby settlements as the threshold changes. Baseline-unreachable settlements lack an identified change in disruption, so their exclusion narrows the population represented by accessibility outcomes rather than indicating that they face no access problem.
~~~~

- After:

~~~~text
The same-local-unit rule leaves 29,133 of the unallocated people within 3 km of a settlement across a unit boundary. Changing the allocation threshold changes represented population without moving already assigned cells between settlements. Priorities therefore describe represented settlements with baseline access; unallocated and baseline-ineligible groups require a separate access-needs assessment.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Population"
     - After: "The same-local-unit rule leaves 29,133 of the unallocated people within 3 km of a settlement across a unit boundary. Changing the"
  2. `replace`
     - Before: "excludes"
     - After: "threshold"
  3. `replace`
     - Before: "people beyond the selected distance and may redistribute"
     - After: "changes"
  4. `replace`
     - Before: "among"
     - After: "without"
  5. `replace`
     - Before: "nearby"
     - After: "moving already assigned cells between settlements. Priorities therefore describe represented"
  6. `replace`
     - Before: "as"
     - After: "with"
  7. `replace`
     - Before: "the threshold changes. Baseline-unreachable settlements lack an identified change in disruption, so their exclusion narrows the population represented by accessibility outcomes rather than indicating that they face no"
     - After: "baseline"
  8. `insert`
     - Before: ""
     - After: ";"
  9. `replace`
     - Before: "problem"
     - After: "unallocated and baseline-ineligible groups require a separate access-needs assessment"

## reviewer-4/comment-7

### part-01

- Location: Abstract (body paragraph index 12, zero-based)
- Reason: 纠正有效状态与inactive的层级，保留摘要其余发现。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:39Z
- Author: Mike Li
- Markup SHA-256 before: `d9b93892c1514067d88bfc187cd852caaf04e1f266e9bf57b24c1abf17c1a96d`
- Markup SHA-256 after: `8fde3444d8fee4ff2265468e43c0e364f9cce79eeb44d94d22314f11c13874a7`
- Revision IDs: `290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165840091617.reviewer-4-comment-7.part-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The 192 nominal structural combinations yield ten effective accessibility states: hazard threshold, facility availability, and settlement snapping change downstream outcomes, while the tested road-closure and topology contrasts are inactive.
~~~~

- After:

~~~~text
The 192 nominal structural combinations yield 24 settlement-vector profiles and ten aggregate profiles; road closure and topology change graph structure but leave the three population-loss aggregates unchanged.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "ten"
     - After: "24"
  2. `replace`
     - Before: "effective"
     - After: "settlement-vector"
  3. `replace`
     - Before: "accessibility states: hazard threshold, facility availability,"
     - After: "profiles"
  4. `replace`
     - Before: "settlement"
     - After: "ten"
  5. `replace`
     - Before: "snapping"
     - After: "aggregate"
  6. `replace`
     - Before: "change"
     - After: "profiles;"
  7. `replace`
     - Before: "downstream"
     - After: "road"
  8. `replace`
     - Before: "outcomes, while the tested road-closure"
     - After: "closure"
  9. `replace`
     - Before: "contrasts"
     - After: "change"
  10. `replace`
     - Before: "are"
     - After: "graph"
  11. `replace`
     - Before: "inactive"
     - After: "structure but leave the three population-loss aggregates unchanged"

### part-02

- Location: Introduction / contributions (body paragraph index 28, zero-based)
- Reason: 贡献陈述与经过核验的状态定义一致。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:40Z
- Author: Mike Li
- Markup SHA-256 before: `8fde3444d8fee4ff2265468e43c0e364f9cce79eeb44d94d22314f11c13874a7`
- Markup SHA-256 after: `a6ef622dea51bafbafa4ad4ca943b72de328432d234dbabe384f5f6fa8f77b1a`
- Revision IDs: `312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165840696636.reviewer-4-comment-7.part-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
This audit reveals ten effective accessibility states across 192 nominal combinations and identifies two inactive structural factors.
~~~~

- After:

~~~~text
This audit distinguishes 24 settlement-vector profiles from ten aggregate profiles across 192 nominal combinations and separates graph activity from changes in population loss.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "reveals"
     - After: "distinguishes 24 settlement-vector profiles from"
  2. `replace`
     - Before: "effective"
     - After: "aggregate"
  3. `replace`
     - Before: "accessibility states"
     - After: "profiles"
  4. `replace`
     - Before: "identifies"
     - After: "separates"
  5. `replace`
     - Before: "two"
     - After: "graph"
  6. `replace`
     - Before: "inactive"
     - After: "activity"
  7. `replace`
     - Before: "structural"
     - After: "from"
  8. `replace`
     - Before: "factors"
     - After: "changes in population loss"

### part-03

- Location: Methodology / Priority Robustness (body paragraph index 91, zero-based)
- Reason: 只更正重复对象，不改min–max排序规则。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:41Z
- Author: Mike Li
- Markup SHA-256 before: `a6ef622dea51bafbafa4ad4ca943b72de328432d234dbabe384f5f6fa8f77b1a`
- Markup SHA-256 after: `21fe01a4a7cba053548aec7fcd4a615f1818ddbbed6dcdc5d4222c69a78e50a8`
- Revision IDs: `328, 329, 330, 331`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165841228361.reviewer-4-comment-7.part-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Structural sensitivity is summarized differently because the factorial contains repeated effective states: we report each settlement's minimum and maximum eligible structural rank.
~~~~

- After:

~~~~text
Structural sensitivity is summarized differently because the factorial contains repeated aggregate outcomes: we report each settlement's minimum and maximum eligible structural rank.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "effective"
     - After: "aggregate"
  2. `replace`
     - Before: "states"
     - After: "outcomes"

### part-04

- Location: Methodology / structural audit (body paragraph index 92, zero-based)
- Reason: 给出完整图、目的地、资格、逐聚落路径及汇总量的独立判据和精度。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:41Z
- Author: Mike Li
- Markup SHA-256 before: `21fe01a4a7cba053548aec7fcd4a615f1818ddbbed6dcdc5d4222c69a78e50a8`
- Markup SHA-256 after: `8de556dadf012dda79ee5af35664282cb1da21e38a65438f06d665c19659395f`
- Revision IDs: `332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165841896785.reviewer-4-comment-7.part-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The structural audit uses paired comparisons that hold four factors fixed while changing the fifth. For each factor, we count comparisons that alter graph state, accessibility outcomes, top-ten membership, or top-ten order. The 192 nominal combinations are also collapsed by their aggregate isolation, delay, and person-minute outcomes to count effective states. This procedure detects factors that change upstream graph representations without changing the downstream estimand. It also avoids treating duplicated outcome states as independent replications. Appendix Table A1 reports the complete factor-activity summary.
~~~~

- After:

~~~~text
The structural audit uses paired comparisons that hold four factors fixed while changing the fifth. For each factor, we separately compare pre-event and post-closure edge sets, connected-component partitions, retained service-node sets, baseline eligibility, settlement-level baseline and disrupted travel times, and access loss. We also count changes in the three population aggregates, top-ten membership, and top-ten order. Distinct graph, settlement-vector, and aggregate profiles are counted separately. Settlement-vector fingerprints combine eligibility with baseline and disrupted travel times and loss rounded to eight decimal places in minutes; aggregate profiles round isolation, delay, and person-minute outcomes to three decimals. An unchanged aggregate profile can therefore contain different graphs or settlement coverage. Appendix Table A1 reports the complete factor-activity summary.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "separately compare pre-event and post-closure edge sets, connected-component partitions, retained service-node sets, baseline eligibility, settlement-level baseline and disrupted travel times, and access loss. We also "
  2. `replace`
     - Before: "comparisons"
     - After: "changes"
  3. `replace`
     - Before: "that"
     - After: "in"
  4. `replace`
     - Before: "alter"
     - After: "the"
  5. `replace`
     - Before: "graph"
     - After: "three"
  6. `replace`
     - Before: "state,"
     - After: "population"
  7. `replace`
     - Before: "accessibility outcomes"
     - After: "aggregates"
  8. `replace`
     - Before: "or"
     - After: "and"
  9. `replace`
     - Before: "The"
     - After: "Distinct"
  10. `replace`
     - Before: "192"
     - After: "graph,"
  11. `replace`
     - Before: "nominal"
     - After: "settlement-vector,"
  12. `replace`
     - Before: "combinations"
     - After: "and aggregate profiles"
  13. `replace`
     - Before: "also"
     - After: "counted"
  14. `replace`
     - Before: "collapsed"
     - After: "separately."
  15. `replace`
     - Before: "by"
     - After: "Settlement-vector"
  16. `replace`
     - Before: "their"
     - After: "fingerprints combine eligibility with baseline and disrupted travel times and loss rounded to eight decimal places in minutes;"
  17. `insert`
     - Before: ""
     - After: " profiles round"
  18. `replace`
     - Before: "count"
     - After: "three"
  19. `replace`
     - Before: "effective states"
     - After: "decimals"
  20. `replace`
     - Before: "This"
     - After: "An"
  21. `replace`
     - Before: "procedure"
     - After: "unchanged"
  22. `replace`
     - Before: "detects"
     - After: "aggregate"
  23. `replace`
     - Before: "factors"
     - After: "profile"
  24. `replace`
     - Before: "that"
     - After: "can"
  25. `replace`
     - Before: "change"
     - After: "therefore"
  26. `replace`
     - Before: "upstream"
     - After: "contain"
  27. `replace`
     - Before: "graph"
     - After: "different"
  28. `replace`
     - Before: "representations"
     - After: "graphs"
  29. `replace`
     - Before: "without"
     - After: "or"
  30. `replace`
     - Before: "changing"
     - After: "settlement"
  31. `replace`
     - Before: "the downstream estimand. It also avoids treating duplicated outcome states as independent replications"
     - After: "coverage"

### part-05

- Location: Results / Network Disruption and Service-Access Loss / second paragraph (body paragraph index 112, zero-based)
- Reason: 保留主结果和已有最大人口变化，纠正拓扑不变并报告实际新增闭路边与连接边。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:42Z
- Author: Mike Li
- Markup SHA-256 before: `8de556dadf012dda79ee5af35664282cb1da21e38a65438f06d665c19659395f`
- Markup SHA-256 after: `d837269278096a0f7ad0c783cf84988ad253a0b3e480017a2a582ed9c67a8a1b`
- Revision IDs: `392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165842591854.reviewer-4-comment-7.part-05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The primary scenario places 24,488 people in settlements with delays longer than five minutes and produces 540,233 person-minutes of positive finite loss. Paired comparisons reveal distinct roles for the five structural factors. Changing the hazard threshold affects access outcomes across all 64 matched groups, with maximum changes of 1,394 delayed people and 70,426 person-minutes, but no change in the newly isolated population. Facility availability is access-active in 32 of 96 groups and changes delayed population by as much as 1,394 people. Settlement snapping is active in all 48 matched groups, with maximum changes of 225 newly isolated people and 13,448 person-minutes. The broader road-closure rule alters as many as 147 closed edges yet produces no change in access outcomes across its 96 paired groups, and the tested topology thresholds alter neither the graph nor access outcomes. These results define the factorial as a factor-activity audit and identify closure rule and topology threshold as inactive over the tested data support. Appendix Table A1 reports the complete paired diagnostics.
~~~~

- After:

~~~~text
The primary scenario places 24,488 people in settlements with delays longer than five minutes and produces 540,233 person-minutes of positive finite loss. Paired comparisons reveal distinct roles for the five structural factors. Changing the hazard threshold affects aggregate access outcomes across all 64 matched groups, with maximum changes of 1,394 delayed people and 70,426 person-minutes, but no change in the newly isolated population. Facility availability is aggregate-active in 32 of 96 groups and changes delayed population by as much as 1,394 people. Settlement snapping changes aggregates in all 48 matched groups, with maximum changes of 225 newly isolated people and 13,448 person-minutes. The broader road-closure rule adds 42, 119, and 147 closures at minimum classes 3, 2, and 1, respectively, but preserves eligible-settlement reachability and finite travel times in all 96 paired groups. Topology repair includes 0, 7, 25, and 73 connectors at 0, 5, 10, and 20 m, producing four baseline graphs; at 3 km snapping, baseline-eligible settlements increase from 609 to 610. These topology and coverage changes leave all three population-loss aggregates unchanged, and Appendix Table A1 separates graph, service, eligibility, settlement-vector, and aggregate activity.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "aggregate "
  2. `replace`
     - Before: "access-active"
     - After: "aggregate-active"
  3. `replace`
     - Before: "is"
     - After: "changes"
  4. `replace`
     - Before: "active"
     - After: "aggregates"
  5. `replace`
     - Before: "alters"
     - After: "adds"
  6. `replace`
     - Before: "as"
     - After: "42,"
  7. `replace`
     - Before: "many"
     - After: "119,"
  8. `replace`
     - Before: "as"
     - After: "and"
  9. `replace`
     - Before: "closed"
     - After: "closures"
  10. `replace`
     - Before: "edges"
     - After: "at"
  11. `replace`
     - Before: "yet"
     - After: "minimum"
  12. `replace`
     - Before: "produces"
     - After: "classes"
  13. `replace`
     - Before: "no"
     - After: "3,"
  14. `replace`
     - Before: "change"
     - After: "2, and 1, respectively, but preserves eligible-settlement reachability and finite travel times"
  15. `replace`
     - Before: "access outcomes across its"
     - After: "all"
  16. `insert`
     - Before: ""
     - After: ". Topology repair includes 0, 7, 25"
  17. `replace`
     - Before: "the"
     - After: "73"
  18. `replace`
     - Before: "tested"
     - After: "connectors"
  19. `replace`
     - Before: "topology"
     - After: "at"
  20. `replace`
     - Before: "thresholds"
     - After: "0,"
  21. `replace`
     - Before: "alter"
     - After: "5,"
  22. `replace`
     - Before: "neither"
     - After: "10,"
  23. `replace`
     - Before: "the"
     - After: "and"
  24. `replace`
     - Before: "graph"
     - After: "20"
  25. `replace`
     - Before: "nor"
     - After: "m,"
  26. `replace`
     - Before: "access"
     - After: "producing"
  27. `replace`
     - Before: "outcomes"
     - After: "four baseline graphs; at 3 km snapping, baseline-eligible settlements increase from 609 to 610"
  28. `replace`
     - Before: "results define the factorial as a factor-activity audit"
     - After: "topology"
  29. `replace`
     - Before: "identify"
     - After: "coverage"
  30. `replace`
     - Before: "closure"
     - After: "changes"
  31. `replace`
     - Before: "rule"
     - After: "leave all three population-loss aggregates unchanged,"
  32. `delete`
     - Before: " topology threshold as inactive over the tested data support."
     - After: ""
  33. `replace`
     - Before: "reports"
     - After: "separates"
  34. `replace`
     - Before: "the"
     - After: "graph,"
  35. `replace`
     - Before: "complete"
     - After: "service,"
  36. `replace`
     - Before: "paired"
     - After: "eligibility,"
  37. `replace`
     - Before: "diagnostics"
     - After: "settlement-vector, and aggregate activity"

### part-06

- Location: Results / Priority Robustness / opening four sentences (body paragraph index 122, zero-based)
- Reason: 分别列出图、聚落、汇总状态，明确全192组合中成员相同但顺序有三种；保留后续rank ranges和其他稳健性家族。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:43Z
- Author: Mike Li
- Markup SHA-256 before: `d837269278096a0f7ad0c783cf84988ad253a0b3e480017a2a582ed9c67a8a1b`
- Markup SHA-256 after: `a195ad85b88e13d2d177be2b53f709c2cf6a69f89fcace5ba58818e65012433e`
- Revision IDs: `463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165843297188.reviewer-4-comment-7.part-06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The structural factorial contains 192 nominal combinations but only ten distinct aggregate accessibility states. Across those states, the identity of the top-ten settlements never change, while three orderings occur. Hazard threshold changes the top-ten order in 32 of 64 paired groups, and settlement snapping changes the order in 16 of 48 groups. Facility availability changes aggregate accessibility in one-third of its paired groups but does not change the displayed top-ten order; the road-closure rule and topology threshold are inactive for every downstream access outcome tested.
~~~~

- After:

~~~~text
The structural factorial contains 192 nominal combinations, four baseline graphs, 24 post-closure graphs, 24 settlement-vector profiles, and ten aggregate profiles. Across all 192 combinations, top-ten membership is invariant, while three orderings occur. Hazard threshold changes the top-ten order in 32 of 64 paired groups, and settlement snapping changes the order in 16 of 48 groups. Facility availability changes aggregate accessibility in 32 of 96 paired groups without changing top-ten order; topology changes eligibility and settlement vectors in all 48 matched groups without changing the loss aggregates.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: ","
  2. `replace`
     - Before: "but"
     - After: "four"
  3. `replace`
     - Before: "only"
     - After: "baseline graphs, 24 post-closure graphs, 24 settlement-vector profiles, and"
  4. `delete`
     - Before: "distinct "
     - After: ""
  5. `replace`
     - Before: "accessibility states"
     - After: "profiles"
  6. `replace`
     - Before: "those"
     - After: "all"
  7. `replace`
     - Before: "states"
     - After: "192 combinations"
  8. `delete`
     - Before: " the identity of the"
     - After: ""
  9. `replace`
     - Before: "settlements"
     - After: "membership"
  10. `replace`
     - Before: "never"
     - After: "is"
  11. `replace`
     - Before: "change"
     - After: "invariant"
  12. `replace`
     - Before: "one-third"
     - After: "32"
  13. `replace`
     - Before: "its"
     - After: "96"
  14. `replace`
     - Before: "but"
     - After: "without"
  15. `replace`
     - Before: "does not change the displayed"
     - After: "changing"
  16. `replace`
     - Before: "the"
     - After: "topology"
  17. `replace`
     - Before: "road-closure"
     - After: "changes"
  18. `replace`
     - Before: "rule"
     - After: "eligibility"
  19. `replace`
     - Before: "topology"
     - After: "settlement"
  20. `replace`
     - Before: "threshold"
     - After: "vectors"
  21. `replace`
     - Before: "are"
     - After: "in"
  22. `replace`
     - Before: "inactive"
     - After: "all"
  23. `replace`
     - Before: "for"
     - After: "48"
  24. `replace`
     - Before: "every"
     - After: "matched"
  25. `replace`
     - Before: "downstream"
     - After: "groups"
  26. `replace`
     - Before: "access"
     - After: "without"
  27. `replace`
     - Before: "outcome"
     - After: "changing"
  28. `replace`
     - Before: "tested"
     - After: "the loss aggregates"

### part-07

- Location: Results / Road-Repair Screening / portfolio interpretation (body paragraph index 126, zero-based)
- Reason: 仅更正重复状态的命名，不改变67%或将十种聚落汇总剖面当修复等价类。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:43Z
- Author: Mike Li
- Markup SHA-256 before: `a195ad85b88e13d2d177be2b53f709c2cf6a69f89fcace5ba58818e65012433e`
- Markup SHA-256 after: `bfd3863f681830f7694297fea436024bb0ef8655bd420d747fec55fe0ffb9b9a`
- Revision IDs: `516, 517, 518, 519`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165843845098.reviewer-4-comment-7.part-07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Given the repeated effective states identified in the factor audit, this percentage describes scenario coverage rather than an engineering probability.
~~~~

- After:

~~~~text
Given the repeated aggregate profiles identified in the factor audit, this percentage describes scenario coverage rather than an engineering probability.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "effective"
     - After: "aggregate"
  2. `replace`
     - Before: "states"
     - After: "profiles"

### part-08

- Location: Discussion / robustness audit paragraph (body paragraph index 141, zero-based)
- Reason: 用完整图和最短路径见证解释汇总量为何不变，删除拓扑早期inactive的错误推论。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:44Z
- Author: Mike Li
- Markup SHA-256 before: `bfd3863f681830f7694297fea436024bb0ef8655bd420d747fec55fe0ffb9b9a`
- Markup SHA-256 after: `f2c97cf762c0220e2a4781b0ddd3099751a82eb4d0c72508fdbfbb91060fa25c`
- Revision IDs: `520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165844626890.reviewer-4-comment-7.part-08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The robustness audit distinguishes active assumptions from nominal variation. Hazard threshold, facility availability, and settlement snapping change at least one accessibility outcome, whereas the tested road-closure rule and topology threshold do not. The inactive closure contrast is informative because it changes the graph by up to 147 closed edges without altering the retained settlement-to-service estimands; the extra candidate edges lie outside the paths that determine those outcomes. Topology repair is inactive earlier in the chain, indicating that the tested thresholds do not create alternative graph states in the processed network. Population allocation and component weighting remain independent sources of rank movement, especially around the top-ten boundary. The ten effective accessibility states, three top-ten orderings, and family-specific intervals provide more interpretable evidence than a pooled frequency over 192 nominal combinations and 10,000 random draws. This structure also identifies where future sensitivity work should concentrate in later analyses: active hazard and service assumptions, population linkage, and preference weights rather than duplicating inactive parameter levels.
~~~~

- After:

~~~~text
The robustness audit distinguishes active assumptions from nominal variation. Hazard threshold, facility availability, and settlement snapping change at least one aggregate access outcome, whereas the tested road-closure rule and topology threshold leave the three population-loss aggregates unchanged. The closure contrast changes component partitions and service travel times at 101–197 graph nodes while preserving the retained settlement-to-service estimands; every eligible settlement with a finite post-disruption path retains an equally short path avoiding the extra closures. Topology repair changes graph connectivity and adds one baseline-eligible settlement with zero event-induced loss, which explains why the loss aggregates remain unchanged. Population allocation and component weighting remain independent sources of rank movement, especially around the top-ten boundary. The 24 settlement-vector profiles, ten aggregate profiles, three top-ten orderings, and family-specific intervals provide more interpretable evidence than a pooled frequency over 192 nominal combinations and 10,000 random draws. This structure directs future sensitivity work toward assumptions that affect each decision outcome and identifies graph or coverage changes that totals alone conceal.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "accessibility"
     - After: "aggregate access"
  2. `replace`
     - Before: "do"
     - After: "leave"
  3. `replace`
     - Before: "not"
     - After: "the three population-loss aggregates unchanged"
  4. `delete`
     - Before: " inactive"
     - After: ""
  5. `delete`
     - Before: "is informative because it "
     - After: ""
  6. `replace`
     - Before: "the"
     - After: "component partitions and service travel times at 101–197"
  7. `replace`
     - Before: "by"
     - After: "nodes"
  8. `replace`
     - Before: "up"
     - After: "while"
  9. `replace`
     - Before: "to 147 closed edges without altering"
     - After: "preserving"
  10. `insert`
     - Before: ""
     - After: "every eligible settlement with a finite post-disruption path retains an equally short path avoiding "
  11. `replace`
     - Before: "candidate edges lie outside the paths that determine those outcomes"
     - After: "closures"
  12. `replace`
     - Before: "is"
     - After: "changes"
  13. `replace`
     - Before: "inactive"
     - After: "graph"
  14. `replace`
     - Before: "earlier"
     - After: "connectivity"
  15. `replace`
     - Before: "in"
     - After: "and adds one baseline-eligible settlement with zero event-induced loss, which explains why"
  16. `replace`
     - Before: "chain,"
     - After: "loss"
  17. `replace`
     - Before: "indicating"
     - After: "aggregates"
  18. `replace`
     - Before: "that"
     - After: "remain"
  19. `replace`
     - Before: "the tested thresholds do not create alternative graph states in the processed network"
     - After: "unchanged"
  20. `insert`
     - Before: ""
     - After: "24 settlement-vector profiles, "
  21. `replace`
     - Before: "effective"
     - After: "aggregate"
  22. `replace`
     - Before: "accessibility states"
     - After: "profiles"
  23. `replace`
     - Before: "also identifies where"
     - After: "directs"
  24. `replace`
     - Before: "should"
     - After: "toward"
  25. `replace`
     - Before: "concentrate"
     - After: "assumptions"
  26. `replace`
     - Before: "in"
     - After: "that"
  27. `replace`
     - Before: "later"
     - After: "affect"
  28. `replace`
     - Before: "analyses:"
     - After: "each"
  29. `replace`
     - Before: "active"
     - After: "decision"
  30. `replace`
     - Before: "hazard"
     - After: "outcome"
  31. `replace`
     - Before: "service"
     - After: "identifies"
  32. `replace`
     - Before: "assumptions,"
     - After: "graph"
  33. `replace`
     - Before: "population"
     - After: "or"
  34. `replace`
     - Before: "linkage,"
     - After: "coverage"
  35. `replace`
     - Before: "and"
     - After: "changes"
  36. `replace`
     - Before: "preference"
     - After: "that"
  37. `replace`
     - Before: "weights"
     - After: "totals"
  38. `replace`
     - Before: "rather"
     - After: "alone"
  39. `replace`
     - Before: "than duplicating inactive parameter levels"
     - After: "conceal"

### part-09

- Location: Conclusion (body paragraph index 149, zero-based)
- Reason: 结论中的状态与activity层级保持准确，其他结论留待相应上游分析完成后处理。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:44Z
- Author: Mike Li
- Markup SHA-256 before: `f2c97cf762c0220e2a4781b0ddd3099751a82eb4d0c72508fdbfbb91060fa25c`
- Markup SHA-256 after: `fbb31c8c56180726dcd7a7b023e786eac046f1b04934842445e2f49314d9877d`
- Revision IDs: `594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T165845184780.reviewer-4-comment-7.part-09.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The 192 structural combinations reduce to ten effective accessibility states: hazard threshold, facility availability, and settlement snapping are active, whereas the tested road-closure and topology contrasts are inactive for the downstream outcomes.
~~~~

- After:

~~~~text
The 192 structural combinations produce 24 settlement-vector profiles and ten aggregate profiles; road closure and topology change graphs without changing the three population-loss aggregates.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "reduce"
     - After: "produce"
  2. `replace`
     - Before: "to"
     - After: "24 settlement-vector profiles and"
  3. `replace`
     - Before: "effective"
     - After: "aggregate"
  4. `replace`
     - Before: "accessibility"
     - After: "profiles;"
  5. `replace`
     - Before: "states:"
     - After: "road"
  6. `replace`
     - Before: "hazard threshold, facility availability, and settlement snapping are active, whereas the tested road-closure"
     - After: "closure"
  7. `replace`
     - Before: "contrasts"
     - After: "change"
  8. `replace`
     - Before: "are"
     - After: "graphs"
  9. `replace`
     - Before: "inactive"
     - After: "without"
  10. `replace`
     - Before: "for"
     - After: "changing"
  11. `replace`
     - Before: "downstream"
     - After: "three"
  12. `replace`
     - Before: "outcomes"
     - After: "population-loss aggregates"

### part-10

- Location: Appendix / Structural and Weighting Robustness / first paragraph (body paragraph index 12, zero-based)
- Reason: 用组件、节点和可行等长路径证明冗余机制，并解释新表列；488为审计人口487.619101的四舍五入。
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:45Z
- Author: Mike Li
- Markup SHA-256 before: `437e3d0ad5cdf48047be8dabf45f3956552813d507dfb0dde4ffee18bcebcd8a`
- Markup SHA-256 after: `3e43fa4210080af7ceccb081946b7e854338dfabfc4945dfde0c5d207bb916d6`
- Revision IDs: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165845682154.reviewer-4-comment-7.part-10.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Appendix Table A1 reports paired activity for the five structural factors while holding the other four fixed. Hazard threshold is graph- and access-active in all 64 paired groups, and facility availability is access-active in 32 of 96 groups. Settlement snapping is access-active in all 48 comparisons despite leaving the closed graph unchanged. Road-closure rule changes graph state in all 96 comparisons but changes no reported access outcome, while topology repair changes neither graph nor access state. No factor changes top-ten membership; hazard threshold changes order in 32 groups and settlement snapping in 16. The full diagnostic sheet retains maximum edge, destination, population, and person-minute changes.
~~~~

- After:

~~~~text
Appendix Table A1 reports matched-group counts separately for post-closure road-edge sets, retained service nodes, baseline eligibility, settlement vectors, aggregate outcomes, top-ten membership, and top-ten order, holding the other four factors fixed. The 0, 5, 10, and 20 m topology thresholds include 0, 7, 25, and 73 connectors and yield 635, 628, 610, and 562 baseline components, counting the same original node universe. At 5 m, settlement OSM 3504477175, with 488 assigned people, becomes baseline eligible with identical baseline and post-disruption travel times of 43.31 minutes and zero event-induced loss. The broader closure rule adds 42, 119, and 147 closed edges at minimum classes 3, 2, and 1, changing component partitions and service travel times at 101, 149, and 197 graph nodes, respectively. Across all 24 topology-by-hazard-by-facility contrasts, shortest-path witnesses for the finite post-disruption paths of baseline-eligible settlements avoid the extra closures, and recomputation confirms identical reachability and travel times. Thus both graph factors alter network structure while the three population-loss aggregates remain unchanged. Top-ten membership persists across all 192 combinations, while hazard threshold changes order in 32 of 64 groups and settlement snapping in 16 of 48; the other factors leave top-ten order unchanged.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "paired"
     - After: "matched-group"
  2. `replace`
     - Before: "activity"
     - After: "counts separately"
  3. `replace`
     - Before: "the"
     - After: "post-closure"
  4. `replace`
     - Before: "five"
     - After: "road-edge"
  5. `replace`
     - Before: "structural"
     - After: "sets,"
  6. `replace`
     - Before: "factors"
     - After: "retained"
  7. `replace`
     - Before: "while"
     - After: "service nodes, baseline eligibility, settlement vectors, aggregate outcomes, top-ten membership, and top-ten order,"
  8. `insert`
     - Before: ""
     - After: "factors "
  9. `replace`
     - Before: "Hazard"
     - After: "The"
  10. `replace`
     - Before: "threshold"
     - After: "0,"
  11. `replace`
     - Before: "is"
     - After: "5,"
  12. `replace`
     - Before: "graph- and access-active in all 64 paired groups"
     - After: "10"
  13. `replace`
     - Before: "facility"
     - After: "20"
  14. `replace`
     - Before: "availability"
     - After: "m"
  15. `replace`
     - Before: "is"
     - After: "topology"
  16. `replace`
     - Before: "access-active"
     - After: "thresholds"
  17. `replace`
     - Before: "in"
     - After: "include"
  18. `replace`
     - Before: "32"
     - After: "0, 7, 25, and 73 connectors and yield 635, 628, 610, and 562 baseline components, counting the same original node universe. At 5 m, settlement OSM 3504477175, with 488 assigned people, becomes baseline eligible with identical baseline and post-disruption travel times"
  19. `replace`
     - Before: "96"
     - After: "43.31"
  20. `replace`
     - Before: "groups"
     - After: "minutes and zero event-induced loss"
  21. `replace`
     - Before: "Settlement"
     - After: "The"
  22. `replace`
     - Before: "snapping"
     - After: "broader"
  23. `replace`
     - Before: "is"
     - After: "closure"
  24. `replace`
     - Before: "access-active"
     - After: "rule"
  25. `replace`
     - Before: "in"
     - After: "adds 42, 119, and 147 closed edges at minimum classes 3, 2, and 1, changing component partitions and service travel times at 101, 149, and 197 graph nodes, respectively. Across"
  26. `replace`
     - Before: "48"
     - After: "24"
  27. `replace`
     - Before: "comparisons"
     - After: "topology-by-hazard-by-facility"
  28. `replace`
     - Before: "despite"
     - After: "contrasts,"
  29. `replace`
     - Before: "leaving"
     - After: "shortest-path witnesses for"
  30. `replace`
     - Before: "closed"
     - After: "finite post-disruption paths of baseline-eligible settlements avoid the extra closures, and recomputation confirms identical reachability and travel times. Thus both"
  31. `insert`
     - Before: ""
     - After: " factors alter network structure while the three population-loss aggregates remain"
  32. `replace`
     - Before: "Road-closure"
     - After: "Top-ten"
  33. `replace`
     - Before: "rule"
     - After: "membership"
  34. `replace`
     - Before: "changes"
     - After: "persists"
  35. `replace`
     - Before: "graph state in"
     - After: "across"
  36. `replace`
     - Before: "96"
     - After: "192"
  37. `replace`
     - Before: "comparisons but changes no reported access outcome"
     - After: "combinations"
  38. `delete`
     - Before: " topology repair changes neither graph nor access state. No factor changes top-ten membership;"
     - After: ""
  39. `insert`
     - Before: ""
     - After: "of 64 "
  40. `insert`
     - Before: ""
     - After: " of 48; the other factors leave top-ten order unchanged"
  41. `delete`
     - Before: " The full diagnostic sheet retains maximum edge, destination, population, and person-minute changes."
     - After: ""

### part-11-cell-r01-c04

- Location: Appendix Table A1, row 1, column 4; Factor / Graph-active
groups
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:45Z
- Author: Mike Li
- Markup SHA-256 before: `3e43fa4210080af7ceccb081946b7e854338dfabfc4945dfde0c5d207bb916d6`
- Markup SHA-256 after: `a66550c4bb9b5ce31bee71d900fa7718f09a5ac45854d540c852e4b56a005afd`
- Revision IDs: `77, 78, 79, 80`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165845944824.reviewer-4-comment-7.part-11-cell-r01-c04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `fb2857a8b887e0be2c40de6b53de2b512efe112a2e31c9ade19290bc8361c2bd`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Graph-active
groups
~~~~

- After:

~~~~text
Road-graph
changes
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Graph-active"
     - After: "Road-graph"
  2. `replace`
     - Before: "groups"
     - After: "changes"

### part-11-cell-r01-c05

- Location: Appendix Table A1, row 1, column 5; Factor / Access-active
groups
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:46Z
- Author: Mike Li
- Markup SHA-256 before: `a66550c4bb9b5ce31bee71d900fa7718f09a5ac45854d540c852e4b56a005afd`
- Markup SHA-256 after: `ae51c3b003a60808f9eb24356a88f2619e978c24aab2812242b85e300ac3e26b`
- Revision IDs: `81, 82, 83, 84`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165846207746.reviewer-4-comment-7.part-11-cell-r01-c05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `fb2857a8b887e0be2c40de6b53de2b512efe112a2e31c9ade19290bc8361c2bd`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Access-active
groups
~~~~

- After:

~~~~text
Service-node
changes
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Access-active"
     - After: "Service-node"
  2. `replace`
     - Before: "groups"
     - After: "changes"

### part-11-cell-r01-c06

- Location: Appendix Table A1, row 1, column 6; Factor / Maximum newly
isolated change
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:46Z
- Author: Mike Li
- Markup SHA-256 before: `ae51c3b003a60808f9eb24356a88f2619e978c24aab2812242b85e300ac3e26b`
- Markup SHA-256 after: `54d6878fc0b7a484b6122a0502cd509e9066317ee8d848a182cb27448ff0baa2`
- Revision IDs: `85, 86, 87, 88`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165846470667.reviewer-4-comment-7.part-11-cell-r01-c06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `fb2857a8b887e0be2c40de6b53de2b512efe112a2e31c9ade19290bc8361c2bd`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Maximum newly
isolated change
~~~~

- After:

~~~~text
Eligibility
changes
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Maximum newly"
     - After: "Eligibility"
  2. `replace`
     - Before: "isolated change"
     - After: "changes"

### part-11-cell-r01-c07

- Location: Appendix Table A1, row 1, column 7; Factor / Maximum delayed
population change
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:46Z
- Author: Mike Li
- Markup SHA-256 before: `54d6878fc0b7a484b6122a0502cd509e9066317ee8d848a182cb27448ff0baa2`
- Markup SHA-256 after: `e799be6e21d0c56c164cf2301affd073a63575340d182676ec8964086e4b9e36`
- Revision IDs: `89, 90, 91, 92`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165846733903.reviewer-4-comment-7.part-11-cell-r01-c07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `fb2857a8b887e0be2c40de6b53de2b512efe112a2e31c9ade19290bc8361c2bd`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Maximum delayed
population change
~~~~

- After:

~~~~text
Settlement-vector
changes
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Maximum delayed"
     - After: "Settlement-vector"
  2. `replace`
     - Before: "population change"
     - After: "changes"

### part-11-cell-r01-c08

- Location: Appendix Table A1, row 1, column 8; Factor / Maximum person-minute
change
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:46Z
- Author: Mike Li
- Markup SHA-256 before: `e799be6e21d0c56c164cf2301affd073a63575340d182676ec8964086e4b9e36`
- Markup SHA-256 after: `be21c6badb5b5450a824b31cfe188b3211845ac37447bd911879ca5e3b8245c7`
- Revision IDs: `93, 94, 95, 96`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165846993905.reviewer-4-comment-7.part-11-cell-r01-c08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `fb2857a8b887e0be2c40de6b53de2b512efe112a2e31c9ade19290bc8361c2bd`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Maximum person-minute
change
~~~~

- After:

~~~~text
Aggregate
changes
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Maximum person-minute"
     - After: "Aggregate"
  2. `replace`
     - Before: "change"
     - After: "changes"

### part-11-cell-r02-c02

- Location: Appendix Table A1, row 2, column 2; Hazard evidence threshold / Levels
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:47Z
- Author: Mike Li
- Markup SHA-256 before: `be21c6badb5b5450a824b31cfe188b3211845ac37447bd911879ca5e3b8245c7`
- Markup SHA-256 after: `1c3ecf93e7cfbe67493845569f8e66ffb1771c7e78c2c950e116a07b55419bfc`
- Revision IDs: `97`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165847248367.reviewer-4-comment-7.part-11-cell-r02-c02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
1, 2, 3
~~~~

- After:

~~~~text
Classes 1, 2, 3
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "Classes "

### part-11-cell-r02-c05

- Location: Appendix Table A1, row 2, column 5; Hazard evidence threshold / Service-node
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:47Z
- Author: Mike Li
- Markup SHA-256 before: `1c3ecf93e7cfbe67493845569f8e66ffb1771c7e78c2c950e116a07b55419bfc`
- Markup SHA-256 after: `740f53712f4112d2c968efa11628851f80d26f9bb48cecb054e54bb7d03981fa`
- Revision IDs: `98, 99`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165847571818.reviewer-4-comment-7.part-11-cell-r02-c05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
64
~~~~

- After:

~~~~text
32
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "64"
     - After: "32"

### part-11-cell-r02-c07

- Location: Appendix Table A1, row 2, column 7; Hazard evidence threshold / Settlement-vector
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:47Z
- Author: Mike Li
- Markup SHA-256 before: `740f53712f4112d2c968efa11628851f80d26f9bb48cecb054e54bb7d03981fa`
- Markup SHA-256 after: `870c58152273c74ee4640d164235adeb0ab59b72a3b1603a9ea90a5a0f40ffee`
- Revision IDs: `100, 101`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165847844743.reviewer-4-comment-7.part-11-cell-r02-c07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
1,394
~~~~

- After:

~~~~text
64
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "1,394"
     - After: "64"

### part-11-cell-r02-c08

- Location: Appendix Table A1, row 2, column 8; Hazard evidence threshold / Aggregate
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:48Z
- Author: Mike Li
- Markup SHA-256 before: `870c58152273c74ee4640d164235adeb0ab59b72a3b1603a9ea90a5a0f40ffee`
- Markup SHA-256 after: `77230fe61d69d8042dcc5c71815e56a27f0598ca80437794bfb1aa4ad42bfa79`
- Revision IDs: `102, 103`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165848118091.reviewer-4-comment-7.part-11-cell-r02-c08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
70,426
~~~~

- After:

~~~~text
64
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "70,426"
     - After: "64"

### part-11-cell-r03-c02

- Location: Appendix Table A1, row 3, column 2; Road closure rule / Levels
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:48Z
- Author: Mike Li
- Markup SHA-256 before: `77230fe61d69d8042dcc5c71815e56a27f0598ca80437794bfb1aa4ad42bfa79`
- Markup SHA-256 after: `7a87846ad4245e0f7333b0259c9f4a6a511c753000a6f3bf9d72df71a391a94d`
- Revision IDs: `104, 105`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165848381697.reviewer-4-comment-7.part-11-cell-r03-c02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
All disruption candidates | Destroyed only
~~~~

- After:

~~~~text
Destroyed only / all candidates
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "All disruption candidates | "
     - After: ""
  2. `insert`
     - Before: ""
     - After: " / all candidates"

### part-11-cell-r04-c02

- Location: Appendix Table A1, row 4, column 2; Facility availability / Levels
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:48Z
- Author: Mike Li
- Markup SHA-256 before: `7a87846ad4245e0f7333b0259c9f4a6a511c753000a6f3bf9d72df71a391a94d`
- Markup SHA-256 after: `9b50205d7c452643d3e641a10694a683f60cb63f77d2a158cea2025fc247f344`
- Revision IDs: `106, 107, 108, 109, 110, 111, 112, 113`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165848654029.reviewer-4-comment-7.part-11-cell-r04-c02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Road and directly exposed facility disruption | Road disruption only
~~~~

- After:

~~~~text
All retained / exposed removed
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Road"
     - After: "All"
  2. `replace`
     - Before: "and"
     - After: "retained"
  3. `replace`
     - Before: "directly"
     - After: "/"
  4. `replace`
     - Before: "facility disruption | Road disruption only"
     - After: "removed"

### part-11-cell-r04-c04

- Location: Appendix Table A1, row 4, column 4; Facility availability / Road-graph
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:48Z
- Author: Mike Li
- Markup SHA-256 before: `9b50205d7c452643d3e641a10694a683f60cb63f77d2a158cea2025fc247f344`
- Markup SHA-256 after: `a4b1b91d607c6fb9604d4057569f4403905f1269a16f2e2bb8974bb89c7a3506`
- Revision IDs: `114, 115`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165848914229.reviewer-4-comment-7.part-11-cell-r04-c04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
96
~~~~

- After:

~~~~text
0
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "96"
     - After: "0"

### part-11-cell-r04-c05

- Location: Appendix Table A1, row 4, column 5; Facility availability / Service-node
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:49Z
- Author: Mike Li
- Markup SHA-256 before: `a4b1b91d607c6fb9604d4057569f4403905f1269a16f2e2bb8974bb89c7a3506`
- Markup SHA-256 after: `46a8b2518640cd6994214f68d32eac68a3c8f9f0b847741103293e48785950aa`
- Revision IDs: `116, 117`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165849173405.reviewer-4-comment-7.part-11-cell-r04-c05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
32
~~~~

- After:

~~~~text
96
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "32"
     - After: "96"

### part-11-cell-r04-c07

- Location: Appendix Table A1, row 4, column 7; Facility availability / Settlement-vector
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:49Z
- Author: Mike Li
- Markup SHA-256 before: `46a8b2518640cd6994214f68d32eac68a3c8f9f0b847741103293e48785950aa`
- Markup SHA-256 after: `cc3502c990b017c237eed6220170a569a2450823970f850d256f6441f980cbb8`
- Revision IDs: `118, 119`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165849450267.reviewer-4-comment-7.part-11-cell-r04-c07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
1,394
~~~~

- After:

~~~~text
32
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "1,394"
     - After: "32"

### part-11-cell-r04-c08

- Location: Appendix Table A1, row 4, column 8; Facility availability / Aggregate
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:49Z
- Author: Mike Li
- Markup SHA-256 before: `cc3502c990b017c237eed6220170a569a2450823970f850d256f6441f980cbb8`
- Markup SHA-256 after: `8c9ea09799a5f5275466c32361f166a5b75bd4cbe2cca77e9f12a1dfc925bfa3`
- Revision IDs: `120, 121`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165849719728.reviewer-4-comment-7.part-11-cell-r04-c08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
33,705
~~~~

- After:

~~~~text
32
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "33,705"
     - After: "32"

### part-11-cell-r05-c02

- Location: Appendix Table A1, row 5, column 2; Topology repair threshold / Levels
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:49Z
- Author: Mike Li
- Markup SHA-256 before: `8c9ea09799a5f5275466c32361f166a5b75bd4cbe2cca77e9f12a1dfc925bfa3`
- Markup SHA-256 after: `a67957ec6c491ac3aa40b5fba5b989ec4e5e84276a9eddd88123fd83de833ffd`
- Revision IDs: `122`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165849988121.reviewer-4-comment-7.part-11-cell-r05-c02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0, 5, 10, 20
~~~~

- After:

~~~~text
0, 5, 10, 20 m
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " m"

### part-11-cell-r05-c04

- Location: Appendix Table A1, row 5, column 4; Topology repair threshold / Road-graph
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:50Z
- Author: Mike Li
- Markup SHA-256 before: `a67957ec6c491ac3aa40b5fba5b989ec4e5e84276a9eddd88123fd83de833ffd`
- Markup SHA-256 after: `162d264faf38cdc988f21c091681a489d1d29a199edfbe400cbf9d169f8dc2ea`
- Revision IDs: `123, 124`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165850254785.reviewer-4-comment-7.part-11-cell-r05-c04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0
~~~~

- After:

~~~~text
48
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "48"

### part-11-cell-r05-c06

- Location: Appendix Table A1, row 5, column 6; Topology repair threshold / Eligibility
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:50Z
- Author: Mike Li
- Markup SHA-256 before: `162d264faf38cdc988f21c091681a489d1d29a199edfbe400cbf9d169f8dc2ea`
- Markup SHA-256 after: `824fd0625ba905d54234f0309af242446829c3db30b22da6e378ad0dda66776b`
- Revision IDs: `125, 126`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165850519896.reviewer-4-comment-7.part-11-cell-r05-c06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0
~~~~

- After:

~~~~text
48
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "48"

### part-11-cell-r05-c07

- Location: Appendix Table A1, row 5, column 7; Topology repair threshold / Settlement-vector
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:50Z
- Author: Mike Li
- Markup SHA-256 before: `824fd0625ba905d54234f0309af242446829c3db30b22da6e378ad0dda66776b`
- Markup SHA-256 after: `93db2cc4e335b146811d4717d7806ad028a7674ee2839518dc41a124b3618f45`
- Revision IDs: `127, 128`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165850782543.reviewer-4-comment-7.part-11-cell-r05-c07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0
~~~~

- After:

~~~~text
48
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "48"

### part-11-cell-r06-c02

- Location: Appendix Table A1, row 6, column 2; Settlement snap distance / Levels
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:51Z
- Author: Mike Li
- Markup SHA-256 before: `93db2cc4e335b146811d4717d7806ad028a7674ee2839518dc41a124b3618f45`
- Markup SHA-256 after: `9b83f91f06092d2c888f0c88c64082816cd922a287d5165e74249dfd5134d137`
- Revision IDs: `129`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165851048460.reviewer-4-comment-7.part-11-cell-r06-c02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
500, 1000, 2000, 3000
~~~~

- After:

~~~~text
500, 1000, 2000, 3000 m
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " m"

### part-11-cell-r06-c05

- Location: Appendix Table A1, row 6, column 5; Settlement snap distance / Service-node
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:51Z
- Author: Mike Li
- Markup SHA-256 before: `9b83f91f06092d2c888f0c88c64082816cd922a287d5165e74249dfd5134d137`
- Markup SHA-256 after: `072bfc8a088212b9a1b2c280f8b2a5dbe28c1fe9065e40b3b0556cbaf5ad8242`
- Revision IDs: `130, 131`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165851311799.reviewer-4-comment-7.part-11-cell-r06-c05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
48
~~~~

- After:

~~~~text
0
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "48"
     - After: "0"

### part-11-cell-r06-c06

- Location: Appendix Table A1, row 6, column 6; Settlement snap distance / Eligibility
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:51Z
- Author: Mike Li
- Markup SHA-256 before: `072bfc8a088212b9a1b2c280f8b2a5dbe28c1fe9065e40b3b0556cbaf5ad8242`
- Markup SHA-256 after: `06bd61eaeb4cc82faa9b52a7e0be16640d14be695344bb823365485819bc2a47`
- Revision IDs: `132, 133`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165851592033.reviewer-4-comment-7.part-11-cell-r06-c06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
225
~~~~

- After:

~~~~text
48
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "225"
     - After: "48"

### part-11-cell-r06-c07

- Location: Appendix Table A1, row 6, column 7; Settlement snap distance / Settlement-vector
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:51Z
- Author: Mike Li
- Markup SHA-256 before: `06bd61eaeb4cc82faa9b52a7e0be16640d14be695344bb823365485819bc2a47`
- Markup SHA-256 after: `cdfc8b30d04ef93e383219b9ad77d1298787c68e2ce8c9905fc12bdf5335e243`
- Revision IDs: `134, 135`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165851873585.reviewer-4-comment-7.part-11-cell-r06-c07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
409
~~~~

- After:

~~~~text
48
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "409"
     - After: "48"

### part-11-cell-r06-c08

- Location: Appendix Table A1, row 6, column 8; Settlement snap distance / Aggregate
changes
- Reason: Implement only the previously presented Table A1 cell content; retain native table structure and hard line breaks.
- Kila decisions: KILA-D-20261023-008
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T07:58:52Z
- Author: Mike Li
- Markup SHA-256 before: `cdfc8b30d04ef93e383219b9ad77d1298787c68e2ce8c9905fc12bdf5335e243`
- Markup SHA-256 after: `2d110ff77689616196f9890da8724c873390d639cf7a8b7d5d8589d8f983748f`
- Revision IDs: `136, 137`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T165852140453.reviewer-4-comment-7.part-11-cell-r06-c08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
13,448
~~~~

- After:

~~~~text
48
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "13,448"
     - After: "48"

