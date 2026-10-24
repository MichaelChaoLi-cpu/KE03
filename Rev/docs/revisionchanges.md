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

## reviewer-4/comment-4

### item-01

- Location: Approved item 1/24: KE03 / Abstract
- Reason: 仅同步本次已验证主定义的数字、权重保持率及前向序列的证据范围；不重写全稿贡献或把本轮当作最终framing。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:16:05Z
- Author: Mike Li
- Markup SHA-256 before: `fbb31c8c56180726dcd7a7b023e786eac046f1b04934842445e2f49314d9877d`
- Markup SHA-256 after: `03decc4c193656918dccbc4139575d8b3f5dde086dbde177746f0c40339a688c`
- Revision IDs: `618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231606217757.reviewer-4-comment-4.item-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Mountain disasters can isolate communities beyond the directly affected area when few road failures disrupt access to essential services. We develop an applied spatial decision framework for the 26 August 2026 rock-ice avalanche and flood corridor in Nepal by linking multi-source event evidence, 767 settlements, calibrated population data, road-network disruption, and a supported-domain survey context. The primary scenario newly isolates 13,906 assigned people, delays 24,488 by more than five minutes, and produces 540,233 person-minutes of finite accessibility loss. The 192 nominal structural combinations yield 24 settlement-vector profiles and ten aggregate profiles; road closure and topology change graph structure but leave the three population-loss aggregates unchanged. Devighat, Bhainse, Naubisephat, and Betrawati lead the settlement priority ranking and remain fixed across eligible structural states and all allocation and weighting specifications. Joint rerouting identifies one road section that reconnects 2,678 people and a second that supplies 121,986 person-minutes of finite improvement, with the modeled benefit plateau reached at two sections. The framework creates a transparent verification queue; current road and facility status, local population and needs, engineering feasibility, and climate attribution require independent evidence.
~~~~

- After:

~~~~text
Mountain disasters can isolate communities beyond the directly affected area when few road failures disrupt access to essential services. We develop an applied spatial decision framework for the 26 August 2026 rock-ice avalanche and flood corridor in Nepal by linking multi-source event evidence, 767 settlements, calibrated population data, road-network disruption, and a supported-domain survey context. The primary scenario newly isolates 13,906 assigned people, delays 34,260 by more than five minutes, and produces 762,097 person-minutes of finite accessibility loss. The 192 nominal structural combinations yield 24 settlement-vector profiles and ten aggregate profiles; road closure and topology change graph structure but leave the three population-loss aggregates unchanged. Devighat, Bhainse, Naubisephat, and Betrawati lead the settlement priority ranking and retain their positions across eligible structural states. All four remain in the top ten under every allocation threshold; weight-rule top-ten persistence is 100% for the first three and 99.85% for Betrawati. Joint rerouting identifies one road section that reconnects 2,678 people and a second that supplies 55,087 person-minutes of finite improvement, with the modeled benefit plateau reached at two sections along the evaluated forward sequence. The framework creates a transparent verification queue; current road and facility status, local population and needs, engineering feasibility, and climate attribution require independent evidence.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "24"
     - After: "34"
  2. `replace`
     - Before: "488"
     - After: "260"
  3. `replace`
     - Before: "540"
     - After: "762"
  4. `replace`
     - Before: "233"
     - After: "097"
  5. `replace`
     - Before: "remain"
     - After: "retain"
  6. `replace`
     - Before: "fixed"
     - After: "their positions"
  7. `insert`
     - Before: ""
     - After: ". All four remain in the top ten under every allocation threshold; weight-rule top-ten persistence is 100% for the first three"
  8. `replace`
     - Before: "all"
     - After: "99.85%"
  9. `replace`
     - Before: "allocation"
     - After: "for"
  10. `replace`
     - Before: "and weighting specifications"
     - After: "Betrawati"
  11. `replace`
     - Before: "121"
     - After: "55"
  12. `replace`
     - Before: "986"
     - After: "087"
  13. `insert`
     - Before: ""
     - After: " along the evaluated forward sequence"

### item-02

- Location: Approved item 2/24: KE03 / Study Area and Data / Settlements, Roads, Services, and Population / network paragraph
- Reason: 更正目的地记录/节点数，披露正标签审计、临床子集及混合服务的含义；删除被具体定义取代的泛化句，保留CEMS匹配文字和引用。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:16:12Z
- Author: Mike Li
- Markup SHA-256 before: `03decc4c193656918dccbc4139575d8b3f5dde086dbde177746f0c40339a688c`
- Markup SHA-256 after: `2b696205bcbe562e33036e54c0c2ba26a9930865de4722d64a26a18d8e615c68`
- Revision IDs: `642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231612745514.reviewer-4-comment-4.item-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Our pre-event transport representation contains 767 mapped settlements and an undirected routable OpenStreetMap road graph connected to health and emergency services. The destination inventory contains 107 included facility records represented by 101 unique graph nodes within the three-district analysis scope. Under the primary topology and snapping rules, 610 settlements have a finite baseline path, 110 are already unreachable, and 47 lie beyond the 3 km maximum settlement-to-road distance. These categories define the settlements for which disruption-induced delay or isolation can be evaluated before event-linked edges are removed. Travel time is calculated from edge length and an explicit road-class speed lookup, with topology-repair connectors assigned a speed of 10 km/h. The same set of service-node is retained for the primary baseline and disruption comparison. CEMS EMSR927 grades are linked to OSM edges in EPSG:32645 using 20 m buffers around road lines and, for OSM-tagged bridge edges, the nearest CEMS bridge point within 100 m; 700 of 706 road features and 18 of 32 bridge points match the graph. This network representation enables comparison between pre-event and disrupted accessibility (Mager Pozo et al., 2025; Tariverdi et al., 2023; Taylor & Susilawati, 2012). The destination and coverage audit further identifies where later facility-status evidence will directly alter the route calculation.
~~~~

- After:

~~~~text
Our pre-event transport representation contains 767 mapped settlements and an undirected routable OpenStreetMap road graph connected to health and emergency services. An exact-tag audit of 1,255 saved facility points retains 102 records at 97 unique graph nodes, excluding five false-positive records from name/address matches, administrative or veterinary functions, and a negative shelter tag. The mixed inventory includes clinical care, pharmacies, dental and blood-bank services, police, shelters, and a fire station; a separate clinical-only sensitivity retains 39 hospital, clinic, or health-post records at 38 nodes. Under the primary topology and snapping rules, 610 settlements have a finite baseline path, 110 are already unreachable, and 47 lie beyond the 3 km maximum settlement-to-road distance. These categories define the settlements for which disruption-induced delay or isolation can be evaluated before event-linked edges are removed. Travel time is calculated from edge length and an explicit road-class speed lookup, with topology-repair connectors assigned a speed of 10 km/h. The same audited service-node set is retained for the primary baseline and disruption comparison; its members represent broad service endpoints rather than equivalent clinical care, and their operational status and capacity are unverified. CEMS EMSR927 grades are linked to OSM edges in EPSG:32645 using 20 m buffers around road lines and, for OSM-tagged bridge edges, the nearest CEMS bridge point within 100 m; 700 of 706 road features and 18 of 32 bridge points match the graph. This network representation enables comparison between pre-event and disrupted accessibility (Mager Pozo et al., 2025; Tariverdi et al., 2023; Taylor & Susilawati, 2012).
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "The"
     - After: "An"
  2. `replace`
     - Before: "destination"
     - After: "exact-tag"
  3. `replace`
     - Before: "inventory"
     - After: "audit"
  4. `replace`
     - Before: "contains"
     - After: "of"
  5. `replace`
     - Before: "107"
     - After: "1,255"
  6. `replace`
     - Before: "included"
     - After: "saved"
  7. `insert`
     - Before: ""
     - After: "points retains 102 "
  8. `replace`
     - Before: "represented"
     - After: "at"
  9. `replace`
     - Before: "by 101"
     - After: "97"
  10. `insert`
     - Before: ""
     - After: ","
  11. `replace`
     - Before: "within"
     - After: "excluding"
  12. `replace`
     - Before: "the"
     - After: "five"
  13. `replace`
     - Before: "three-district"
     - After: "false-positive"
  14. `replace`
     - Before: "analysis"
     - After: "records"
  15. `replace`
     - Before: "scope"
     - After: "from name/address matches, administrative or veterinary functions, and a negative shelter tag. The mixed inventory includes clinical care, pharmacies, dental and blood-bank services, police, shelters, and a fire station; a separate clinical-only sensitivity retains 39 hospital, clinic, or health-post records at 38 nodes"
  16. `replace`
     - Before: "set of"
     - After: "audited"
  17. `insert`
     - Before: ""
     - After: " set"
  18. `insert`
     - Before: ""
     - After: "; its members represent broad service endpoints rather than equivalent clinical care, and their operational status and capacity are unverified"
  19. `delete`
     - Before: " The destination and coverage audit further identifies where later facility-status evidence will directly alter the route calculation."
     - After: ""

### item-03

- Location: Approved item 3/24: KE03 / Methodology / Cascading-Hazard Evidence Reconstruction / paragraph introducing Equation 2
- Reason: 更正因事后发现分类错误而修订目的地后的时间顺序说明；不改变原hazard/closure/topology/snap主规格或公式。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:16:19Z
- Author: Mike Li
- Markup SHA-256 before: `2b696205bcbe562e33036e54c0c2ba26a9930865de4722d64a26a18d8e615c68`
- Markup SHA-256 after: `ba50f4236950bc75948b99fa0154de00eb9ddea29756cf90a655dfe202b90ac5`
- Revision IDs: `675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231619218233.reviewer-4-comment-4.item-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Equation 2 records the primary scenario before any outcome is examined. It requires the conservative evidence class, removes only road edges graded as destroyed, retains all mapped health and emergency destinations, repairs topology gaps up to the specified threshold, and connects settlements within the specified maximum distance. Alternative scenarios vary one or more of these elements, but primary estimates remain separate from robustness summaries.
~~~~

- After:

~~~~text
Equation 2 records the primary hazard, closure, topology, and snapping settings; the audited destination inventory supplies the service set used in the revised analysis. It requires the conservative evidence class, removes only road edges graded as destroyed, retains all audited health and emergency destinations, repairs topology gaps up to the specified threshold, and connects settlements within the specified maximum distance. Alternative scenarios vary one or more of these elements, but primary estimates remain separate from robustness summaries.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "scenario"
     - After: "hazard,"
  2. `replace`
     - Before: "before"
     - After: "closure,"
  3. `replace`
     - Before: "any"
     - After: "topology,"
  4. `replace`
     - Before: "outcome"
     - After: "and"
  5. `replace`
     - Before: "is"
     - After: "snapping"
  6. `replace`
     - Before: "examined"
     - After: "settings; the audited destination inventory supplies the service set used in the revised analysis"
  7. `replace`
     - Before: "mapped"
     - After: "audited"

### item-04

- Location: Approved item 4/24: KE03 / Methodology / Network Disruption and Service Accessibility / baseline and closure definitions
- Reason: 更正97节点并解释现有速度的建模地位；完整14类lookup及已通过闭路规则不改，保留引用。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:16:25Z
- Author: Mike Li
- Markup SHA-256 before: `ba50f4236950bc75948b99fa0154de00eb9ddea29756cf90a655dfe202b90ac5`
- Markup SHA-256 after: `2d4033d8852a2707206e4cd46211047755f4e7641a24e53a342353c99e365887`
- Revision IDs: `689, 690, 691`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231625818838.reviewer-4-comment-4.item-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Baseline accessibility is the shortest modeled travel time from each eligible settlement node to the nearest of the 101 retained health or emergency service nodes on the pre-event graph (Mager Pozo et al., 2025). Edge time equals length divided by the assigned speed: trunk 60 (trunk-link 40), primary 50 (primary-link 35), secondary 40 (secondary-link 30), tertiary 30 (tertiary-link 25), residential or unclassified 20, service, living-street, or generic road 15, and track 10 km/h; accepted topology connectors also use 10 km/h. For each scenario, an edge is removed only if it belongs to the selected topology-specific graph, intersects a raster cell meeting the hazard-class threshold under all-touched rasterization, and has a qualifying CEMS grade, taking the most severe grade when several features match. The primary rule admits Destroyed, while the broader rule also admits Possibly damaged and Damaged. Qualifying conditions close the entire edge before shortest paths are recalculated, even when only part intersects the selected footprint. Finite delay requires both paths to exist and the disrupted path to be longer. New isolation occurs when a settlement with a finite baseline path has no path to any of its retained destinations after disruption (Mager Pozo et al., 2025). Settlements without a finite baseline path remain in the coverage audit but do not enter change estimates.
~~~~

- After:

~~~~text
Baseline accessibility is the shortest modeled travel time from each eligible settlement node to the nearest of the 97 retained health or emergency service nodes on the pre-event graph (Mager Pozo et al., 2025). Edge time equals length divided by the assigned speed: trunk 60 (trunk-link 40), primary 50 (primary-link 35), secondary 40 (secondary-link 30), tertiary 30 (tertiary-link 25), residential or unclassified 20, service, living-street, or generic road 15, and track 10 km/h; accepted topology connectors also use 10 km/h. The assigned road-class speeds define comparative network costs; local traffic calibration and observed emergency-response times are unavailable. For each scenario, an edge is removed only if it belongs to the selected topology-specific graph, intersects a raster cell meeting the hazard-class threshold under all-touched rasterization, and has a qualifying CEMS grade, taking the most severe grade when several features match. The primary rule admits Destroyed, while the broader rule also admits Possibly damaged and Damaged. Qualifying conditions close the entire edge before shortest paths are recalculated, even when only part intersects the selected footprint. Finite delay requires both paths to exist and the disrupted path to be longer. New isolation occurs when a settlement with a finite baseline path has no path to any of its retained destinations after disruption (Mager Pozo et al., 2025). Settlements without a finite baseline path remain in the coverage audit but do not enter change estimates.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "101"
     - After: "97"
  2. `insert`
     - Before: ""
     - After: ". The assigned road-class speeds define comparative network costs; local traffic calibration and observed emergency-response times are unavailable"

### item-05

- Location: Approved item 5/24: KE03 / Methodology / Network Disruption and Service Accessibility / estimands and sensitivity design
- Reason: 一次完整说明五分钟的报告作用、四套速度、三目的地/两可用性、固定共同样本以及均匀缩放tie处理。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:16:31Z
- Author: Mike Li
- Markup SHA-256 before: `2d4033d8852a2707206e4cd46211047755f4e7641a24e53a342353c99e365887`
- Markup SHA-256 after: `0c766c35b923e8a8b7608beac381bf48934e4e6825eee5bd237558a5eb8d30a1`
- Revision IDs: `692`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231631897061.reviewer-4-comment-4.item-05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Scenario summaries keep finite and infinite path changes separate. Newly Isolated Population sums assigned population at settlements that lose all modeled access, whereas Population Delayed over 5 Minutes sums population at settlements whose finite travel time rises beyond that threshold. Population-Weighted Accessibility Loss multiplies each positive finite delay by assigned settlement population and reports the total in person-minutes. The estimands exclude unallocated population and do not substitute an arbitrary finite penalty for isolation.
~~~~

- After:

~~~~text
Scenario summaries keep finite and infinite path changes separate. Newly Isolated Population sums assigned population at settlements that lose all modeled access, whereas Population Delayed over 5 Minutes sums population at settlements whose finite travel time rises beyond that threshold. Population-Weighted Accessibility Loss multiplies each positive finite delay by assigned settlement population and reports the total in person-minutes. Five minutes is an interpretable reporting category rather than an emergency-response target; continuous losses remain available, and reporting at strictly greater than 2, 5, or 10 minutes does not change routes or scores. We compare reference speeds with uniform 0.75 and 1.25 multipliers on all roads and connectors. A differential slower specification uses multipliers of 0.80 for trunk/primary roads and links, 0.60 for secondary/tertiary roads and links, and 0.50 for local roads, tracks, and connectors, applied equally to baseline and disrupted graphs. The audited mixed, clinical-only, and historical original inventories are each evaluated under all four speed specifications, with destinations retained or directly class-3-exposed records removed before node deduplication. Common-cohort comparisons separate changes in baseline coverage from disruption-induced loss, and uniform scaling retains the reference loss ordering and ties for scoring. The estimands exclude unallocated population and do not substitute an arbitrary finite penalty for isolation.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "Five minutes is an interpretable reporting category rather than an emergency-response target; continuous losses remain available, and reporting at strictly greater than 2, 5, or 10 minutes does not change routes or scores. We compare reference speeds with uniform 0.75 and 1.25 multipliers on all roads and connectors. A differential slower specification uses multipliers of 0.80 for trunk/primary roads and links, 0.60 for secondary/tertiary roads and links, and 0.50 for local roads, tracks, and connectors, applied equally to baseline and disrupted graphs. The audited mixed, clinical-only, and historical original inventories are each evaluated under all four speed specifications, with destinations retained or directly class-3-exposed records removed before node deduplication. Common-cohort comparisons separate changes in baseline coverage from disruption-induced loss, and uniform scaling retains the reference loss ordering and ties for scoring. "

### item-06

- Location: Approved item 6/24: KE03 / Results / Network Disruption and Service-Access Loss / coverage and primary outcomes
- Reason: 只同步新主有限延误人口；人口覆盖分解、闭路数量和新增隔离总量均未变。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:16:48Z
- Author: Mike Li
- Markup SHA-256 before: `0c766c35b923e8a8b7608beac381bf48934e4e6825eee5bd237558a5eb8d30a1`
- Markup SHA-256 after: `fdd42ed8900a08996b3936f1408dd7c0ddaa2a77bbd23d6d5163ac9c12cd960d`
- Revision IDs: `693, 694, 695, 696`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231648271835.reviewer-4-comment-4.item-06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Of the 573,645 assigned people, 532,382 belong to the 610 baseline-eligible settlements, 36,182 to 110 baseline-unreachable settlements within the road-snap limit, and 5,081 to 47 settlements beyond that limit. Evidence-linked closures produce finite delays near the southern corridor and a longer chain of newly isolated settlements toward the north. Figure 2 maps the 2,023 primary-closed graph edges (54.79 km), of which 199 intersect the class-3 footprint only partially, alongside baseline access and post-disruption status. Settlement outcomes depend on each settlement's position within the connected graph and its proximity to communities. Northern settlements lose their modeled paths where a corridor link lacks a retained alternative, whereas connected southern settlements reroute over longer paths. This contrast reflects uneven redundancy along the event corridor. Across eligible settlements, the primary scenario newly isolates 13,906 assigned people, including communities beyond the strongest hazard footprint. Another 24,488 assigned people remain connected but experience delays longer than five minutes. The separation between these two populations prevents a large finite delay from being treated as equivalent to complete disconnection. The spatial pattern identifies corridor links whose field verification can update access estimates for several settlements simultaneously and shows which communities depend on the same high-leverage connection during response.
~~~~

- After:

~~~~text
Of the 573,645 assigned people, 532,382 belong to the 610 baseline-eligible settlements, 36,182 to 110 baseline-unreachable settlements within the road-snap limit, and 5,081 to 47 settlements beyond that limit. Evidence-linked closures produce finite delays near the southern corridor and a longer chain of newly isolated settlements toward the north. Figure 2 maps the 2,023 primary-closed graph edges (54.79 km), of which 199 intersect the class-3 footprint only partially, alongside baseline access and post-disruption status. Settlement outcomes depend on each settlement's position within the connected graph and its proximity to communities. Northern settlements lose their modeled paths where a corridor link lacks a retained alternative, whereas connected southern settlements reroute over longer paths. This contrast reflects uneven redundancy along the event corridor. Across eligible settlements, the primary scenario newly isolates 13,906 assigned people, including communities beyond the strongest hazard footprint. Another 34,260 assigned people remain connected but experience delays longer than five minutes. The separation between these two populations prevents a large finite delay from being treated as equivalent to complete disconnection. The spatial pattern identifies corridor links whose field verification can update access estimates for several settlements simultaneously and shows which communities depend on the same high-leverage connection during response.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "24"
     - After: "34"
  2. `replace`
     - Before: "488"
     - After: "260"

### item-07-atom-001

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:20Z
- Author: Mike Li
- Markup SHA-256 before: `fdd42ed8900a08996b3936f1408dd7c0ddaa2a77bbd23d6d5163ac9c12cd960d`
- Markup SHA-256 after: `c5dd2900f33728015eeda73a5f1dee95d7c5067969c4117fb076df82b363c583`
- Revision IDs: `401`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231921090418.reviewer-4-comment-4.item-07-atom-001.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
separates
~~~~

- After:

~~~~text
and the accompanying structural audit separate
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "separates"
     - After: "and the accompanying structural audit separate"

### item-07-atom-002

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:21Z
- Author: Mike Li
- Markup SHA-256 before: `c5dd2900f33728015eeda73a5f1dee95d7c5067969c4117fb076df82b363c583`
- Markup SHA-256 after: `3f30bda0afd3a3e5ecd2db4ce6b5be7bd74198315a7b1d0b4e7ff2eac9f83fae`
- Revision IDs: `697`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231921790780.reviewer-4-comment-4.item-07-atom-002.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
d, and
~~~~

- After:

~~~~text
d,
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " and"
     - After: ""

### item-07-atom-003

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:22Z
- Author: Mike Li
- Markup SHA-256 before: `3f30bda0afd3a3e5ecd2db4ce6b5be7bd74198315a7b1d0b4e7ff2eac9f83fae`
- Markup SHA-256 after: `2d4a7e8a1ac5c3ee53f84a8cde9f8d3783ee5738c57e849aea76f75d385cc0f7`
- Revision IDs: `404`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231922625242.reviewer-4-comment-4.item-07-atom-003.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
d,
~~~~

- After:

~~~~text
d;
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: ","
     - After: ";"

### item-07-atom-004

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:23Z
- Author: Mike Li
- Markup SHA-256 before: `2d4a7e8a1ac5c3ee53f84a8cde9f8d3783ee5738c57e849aea76f75d385cc0f7`
- Markup SHA-256 after: `81746a95ce2c5a6a7612198a6706d6e80a8c49487a4159c00dbf52e9136c0da4`
- Revision IDs: `404`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231923282913.reviewer-4-comment-4.item-07-atom-004.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
e all
~~~~

- After:

~~~~text
e the
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "all"
     - After: "the"

### item-07-atom-005

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:23Z
- Author: Mike Li
- Markup SHA-256 before: `81746a95ce2c5a6a7612198a6706d6e80a8c49487a4159c00dbf52e9136c0da4`
- Markup SHA-256 after: `8f2d32145e62db89cc7399578405eddd8275ae8d3051baf5621982e7409681de`
- Revision IDs: `408`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231923935881.reviewer-4-comment-4.item-07-atom-005.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
coverage
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "coverage"
     - After: ""

### item-07-atom-006

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:24Z
- Author: Mike Li
- Markup SHA-256 before: `8f2d32145e62db89cc7399578405eddd8275ae8d3051baf5621982e7409681de`
- Markup SHA-256 after: `3bfdfcfbcd0b96d760915671c9d897a8bfb2ef12ca09ba42287cc80cfd6f4c4f`
- Revision IDs: `698`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231924597473.reviewer-4-comment-4.item-07-atom-006.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
gy and 
~~~~

- After:

~~~~text
gy
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " and "
     - After: ""

### item-07-atom-007

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:25Z
- Author: Mike Li
- Markup SHA-256 before: `3bfdfcfbcd0b96d760915671c9d897a8bfb2ef12ca09ba42287cc80cfd6f4c4f`
- Markup SHA-256 after: `1ac18f01d7f05a74ac1e3222279d82385dbfc9e7e029606c14091cdbaa139778`
- Revision IDs: `699`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231925262723.reviewer-4-comment-4.item-07-atom-007.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
. These 
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: ". These "
     - After: ""

### item-07-atom-008

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:25Z
- Author: Mike Li
- Markup SHA-256 before: `1ac18f01d7f05a74ac1e3222279d82385dbfc9e7e029606c14091cdbaa139778`
- Markup SHA-256 after: `04a21d35be05df8ce34f2c2891d0ff89acec9f08b26596defb26aa5999995431`
- Revision IDs: `412`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231925939669.reviewer-4-comment-4.item-07-atom-008.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
four baseline graphs; at 3 km snapping, baseline-eligible settlements increase from 609 to 610
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "four baseline graphs; at 3 km snapping, baseline-eligible settlements increase from 609 to 610"
     - After: ""

### item-07-atom-009

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:26Z
- Author: Mike Li
- Markup SHA-256 before: `04a21d35be05df8ce34f2c2891d0ff89acec9f08b26596defb26aa5999995431`
- Markup SHA-256 after: `37ecff36198efa261a4efc2611ef82c55ba9299c826bc07bf77f7eb9539dbe79`
- Revision IDs: `700`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231926613160.reviewer-4-comment-4.item-07-atom-009.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 to
~~~~

- After:

~~~~text
to
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-010

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:27Z
- Author: Mike Li
- Markup SHA-256 before: `37ecff36198efa261a4efc2611ef82c55ba9299c826bc07bf77f7eb9539dbe79`
- Markup SHA-256 after: `7139037bfcdd5c9c6cbfac72baf88197d153feca7254b11654d4a24a2cf2a800`
- Revision IDs: `414`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231927285191.reviewer-4-comment-4.item-07-atom-010.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
producing
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "producing"
     - After: ""

### item-07-atom-011

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:27Z
- Author: Mike Li
- Markup SHA-256 before: `7139037bfcdd5c9c6cbfac72baf88197d153feca7254b11654d4a24a2cf2a800`
- Markup SHA-256 after: `a476f90e043754f2da27f5a01c988888ca9fda2869a4723d4172edde033599b1`
- Revision IDs: `701`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231927991947.reviewer-4-comment-4.item-07-atom-011.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
m, 
~~~~

- After:

~~~~text
m,
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-012

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:28Z
- Author: Mike Li
- Markup SHA-256 before: `a476f90e043754f2da27f5a01c988888ca9fda2869a4723d4172edde033599b1`
- Markup SHA-256 after: `7278af84f3f50b1216fd115d57268e0adb711053952e296014b1978199f967e1`
- Revision IDs: `416`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231928660997.reviewer-4-comment-4.item-07-atom-012.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
m,
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "m,"
     - After: ""

### item-07-atom-013

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:29Z
- Author: Mike Li
- Markup SHA-256 before: `7278af84f3f50b1216fd115d57268e0adb711053952e296014b1978199f967e1`
- Markup SHA-256 after: `4fae162b803d80c84ee9c2bc83f64d32f683642dc8698cde2631cc8b448077a2`
- Revision IDs: `702`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231929340366.reviewer-4-comment-4.item-07-atom-013.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
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
0
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-014

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:29Z
- Author: Mike Li
- Markup SHA-256 before: `4fae162b803d80c84ee9c2bc83f64d32f683642dc8698cde2631cc8b448077a2`
- Markup SHA-256 after: `480818883d0d0afc03a1e3870aa103237be7ee10cedf49574841b3ade5a6d51e`
- Revision IDs: `418`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231930043339.reviewer-4-comment-4.item-07-atom-014.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
20
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "20"
     - After: ""

### item-07-atom-015

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:30Z
- Author: Mike Li
- Markup SHA-256 before: `480818883d0d0afc03a1e3870aa103237be7ee10cedf49574841b3ade5a6d51e`
- Markup SHA-256 after: `aabf911101a2fadde21cd16807e72eeddf227cb9eb94ae7a2ae221c5a0cb379c`
- Revision IDs: `703`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231930729682.reviewer-4-comment-4.item-07-atom-015.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 to
~~~~

- After:

~~~~text
to
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-016

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:31Z
- Author: Mike Li
- Markup SHA-256 before: `aabf911101a2fadde21cd16807e72eeddf227cb9eb94ae7a2ae221c5a0cb379c`
- Markup SHA-256 after: `91a4e88420e6449a8dced54c3567c56a61279df1e95e7e169654aff862e9e209`
- Revision IDs: `420`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231931380731.reviewer-4-comment-4.item-07-atom-016.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0, and
~~~~

- After:

~~~~text
0, 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "and"
     - After: ""

### item-07-atom-017

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:44Z
- Author: Mike Li
- Markup SHA-256 before: `91a4e88420e6449a8dced54c3567c56a61279df1e95e7e169654aff862e9e209`
- Markup SHA-256 after: `596aba4d1706a7d034d77bd8736cee89fbc5ad8637a5184af9e868291a49f541`
- Revision IDs: `704`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231944395146.reviewer-4-comment-4.item-07-atom-017.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 to
~~~~

- After:

~~~~text
to
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-018

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:44Z
- Author: Mike Li
- Markup SHA-256 before: `596aba4d1706a7d034d77bd8736cee89fbc5ad8637a5184af9e868291a49f541`
- Markup SHA-256 after: `e630ab2f19d0fe51271f5a3bc5f80cf9a43fc3b3f1e9b32182a392f915a026a3`
- Revision IDs: `422`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231945058436.reviewer-4-comment-4.item-07-atom-018.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
10,
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "10,"
     - After: ""

### item-07-atom-019

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:45Z
- Author: Mike Li
- Markup SHA-256 before: `e630ab2f19d0fe51271f5a3bc5f80cf9a43fc3b3f1e9b32182a392f915a026a3`
- Markup SHA-256 after: `e8ef0dd3e6caa1ffe37f4870ae920d3be45ab82a16abdc3f4a1b25dcadd0845e`
- Revision IDs: `705`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231945735331.reviewer-4-comment-4.item-07-atom-019.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
, t
~~~~

- After:

~~~~text
,t
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-020

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:46Z
- Author: Mike Li
- Markup SHA-256 before: `e8ef0dd3e6caa1ffe37f4870ae920d3be45ab82a16abdc3f4a1b25dcadd0845e`
- Markup SHA-256 after: `632094c3e31f8a03bb959d6fd51b74742b01f6315fd0b722b1223e1606fad9be`
- Revision IDs: `424`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231946386877.reviewer-4-comment-4.item-07-atom-020.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 5,
~~~~

- After:

~~~~text
 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "5,"
     - After: ""

### item-07-atom-021

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:46Z
- Author: Mike Li
- Markup SHA-256 before: `632094c3e31f8a03bb959d6fd51b74742b01f6315fd0b722b1223e1606fad9be`
- Markup SHA-256 after: `4db3c54f3f3b9cf6a4c938dd700d5f241eb85b44ddf6f0c7be5a5d118920b4a8`
- Revision IDs: `706`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231947045980.reviewer-4-comment-4.item-07-atom-021.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 to
~~~~

- After:

~~~~text
to
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-022

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:47Z
- Author: Mike Li
- Markup SHA-256 before: `4db3c54f3f3b9cf6a4c938dd700d5f241eb85b44ddf6f0c7be5a5d118920b4a8`
- Markup SHA-256 after: `15d75b5c223ec2c94a0512960d0ba00899393b2b7bd36a3ec25dca5178d303e1`
- Revision IDs: `426`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231947715744.reviewer-4-comment-4.item-07-atom-022.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0,t
~~~~

- After:

~~~~text
t
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "0,"
     - After: ""

### item-07-atom-023

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:48Z
- Author: Mike Li
- Markup SHA-256 before: `15d75b5c223ec2c94a0512960d0ba00899393b2b7bd36a3ec25dca5178d303e1`
- Markup SHA-256 after: `1a86e2f04252aa017368e8c0153a53c2de303f1f29d9679bdda2d504acda5249`
- Revision IDs: `707`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231948378822.reviewer-4-comment-4.item-07-atom-023.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 to
~~~~

- After:

~~~~text
to
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-024

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:48Z
- Author: Mike Li
- Markup SHA-256 before: `1a86e2f04252aa017368e8c0153a53c2de303f1f29d9679bdda2d504acda5249`
- Markup SHA-256 after: `0f836451fd029e42af2442e950eaa92da42e5f07c859fe19b80de98113d3f01e`
- Revision IDs: `428`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231949041114.reviewer-4-comment-4.item-07-atom-024.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
rs at
~~~~

- After:

~~~~text
rs 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "at"
     - After: ""

### item-07-atom-025

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:49Z
- Author: Mike Li
- Markup SHA-256 before: `0f836451fd029e42af2442e950eaa92da42e5f07c859fe19b80de98113d3f01e`
- Markup SHA-256 after: `45a55d734201aeb9fb9d28bf2ede55e750d499eb87180aa1515b14f0c81ae6b0`
- Revision IDs: `708`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231949718056.reviewer-4-comment-4.item-07-atom-025.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 to
~~~~

- After:

~~~~text
to
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-026

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:50Z
- Author: Mike Li
- Markup SHA-256 before: `45a55d734201aeb9fb9d28bf2ede55e750d499eb87180aa1515b14f0c81ae6b0`
- Markup SHA-256 after: `eedca31a69d4317887e22b00cb68505d90a6e9f9e033a6599a16cbf8fe896117`
- Revision IDs: `430`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231950403966.reviewer-4-comment-4.item-07-atom-026.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
connectors
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "connectors"
     - After: ""

### item-07-atom-027

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:50Z
- Author: Mike Li
- Markup SHA-256 before: `eedca31a69d4317887e22b00cb68505d90a6e9f9e033a6599a16cbf8fe896117`
- Markup SHA-256 after: `1f6fee47107d8f02fce16a1cca923ee0a9ddc8b641763092f847dbc973107f98`
- Revision IDs: `709`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231951083779.reviewer-4-comment-4.item-07-atom-027.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
73 
~~~~

- After:

~~~~text
73
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-028

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:51Z
- Author: Mike Li
- Markup SHA-256 before: `1f6fee47107d8f02fce16a1cca923ee0a9ddc8b641763092f847dbc973107f98`
- Markup SHA-256 after: `eaf1e6e20bb3246110aa22231e31dedbb67d2ea6ebfa7fe46fd567e280b2bce6`
- Revision IDs: `432`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231951752178.reviewer-4-comment-4.item-07-atom-028.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
73
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "73"
     - After: ""

### item-07-atom-029

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:52Z
- Author: Mike Li
- Markup SHA-256 before: `eaf1e6e20bb3246110aa22231e31dedbb67d2ea6ebfa7fe46fd567e280b2bce6`
- Markup SHA-256 after: `0b15479981341af33e3c7b73839ebb7ea289ebe28e2c328944f989115eaf6ac7`
- Revision IDs: `710`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231952433363.reviewer-4-comment-4.item-07-atom-029.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
5,
~~~~

- After:

~~~~text
5
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: ","
     - After: ""

### item-07-atom-030

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:52Z
- Author: Mike Li
- Markup SHA-256 before: `0b15479981341af33e3c7b73839ebb7ea289ebe28e2c328944f989115eaf6ac7`
- Markup SHA-256 after: `8e43277c5c82ec105ff6ecb4eddf9f4175309d8b661f68f68fb1ca39d7049a17`
- Revision IDs: `433`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231953103693.reviewer-4-comment-4.item-07-atom-030.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Topology repair includes 0, 7, 25
~~~~

- After:

~~~~text
Road-closure
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Topology repair includes 0, 7, 25"
     - After: "Road-closure"

### item-07-atom-031

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:53Z
- Author: Mike Li
- Markup SHA-256 before: `8e43277c5c82ec105ff6ecb4eddf9f4175309d8b661f68f68fb1ca39d7049a17`
- Markup SHA-256 after: `88b70972934f0dd809737e31f2ab268720467e7edda7bc7223356b18743d789e`
- Revision IDs: `711`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231953781836.reviewer-4-comment-4.item-07-atom-031.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 96 paired
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " 96 paired"
     - After: ""

### item-07-atom-032

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:54Z
- Author: Mike Li
- Markup SHA-256 before: `88b70972934f0dd809737e31f2ab268720467e7edda7bc7223356b18743d789e`
- Markup SHA-256 after: `61052b5999e9ee616c4356f3abfef9a51e9fdf92b1313ee971feed3e9f2b55dc`
- Revision IDs: `435`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231954456270.reviewer-4-comment-4.item-07-atom-032.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
all g
~~~~

- After:

~~~~text
 g
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "all"
     - After: ""

### item-07-atom-033

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:54Z
- Author: Mike Li
- Markup SHA-256 before: `61052b5999e9ee616c4356f3abfef9a51e9fdf92b1313ee971feed3e9f2b55dc`
- Markup SHA-256 after: `b94a1142c8032b37b9f7c016140cdf813c2fab0ecbfe7843420bb44cd9007e93`
- Revision IDs: `712`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231955133567.reviewer-4-comment-4.item-07-atom-033.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
mes in 
~~~~

- After:

~~~~text
mes
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " in "
     - After: ""

### item-07-atom-034

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:55Z
- Author: Mike Li
- Markup SHA-256 before: `b94a1142c8032b37b9f7c016140cdf813c2fab0ecbfe7843420bb44cd9007e93`
- Markup SHA-256 after: `64b4f37399e97669fae528b5f8303cdb85deb8fec0c203df7fc95d7f4cdd7645`
- Revision IDs: `437`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231955793624.reviewer-4-comment-4.item-07-atom-034.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
2, and 1, respectively, but preserves eligible-settlement reachability and finite travel times
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "2, and 1, respectively, but preserves eligible-settlement reachability and finite travel times"
     - After: ""

### item-07-atom-035

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:56Z
- Author: Mike Li
- Markup SHA-256 before: `64b4f37399e97669fae528b5f8303cdb85deb8fec0c203df7fc95d7f4cdd7645`
- Markup SHA-256 after: `d0987f9b91a9cdafbbf97fea54124a8cb1cd15b7a0725fafba492aea80677685`
- Revision IDs: `713`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231956454569.reviewer-4-comment-4.item-07-atom-035.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
3, 
~~~~

- After:

~~~~text
3,
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-036

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:56Z
- Author: Mike Li
- Markup SHA-256 before: `d0987f9b91a9cdafbbf97fea54124a8cb1cd15b7a0725fafba492aea80677685`
- Markup SHA-256 after: `d260f90821c86d679275165daea3e39ab810305e214f662875bd7c97735f9826`
- Revision IDs: `439`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231957112254.reviewer-4-comment-4.item-07-atom-036.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 3,
~~~~

- After:

~~~~text
 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "3,"
     - After: ""

### item-07-atom-037

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:57Z
- Author: Mike Li
- Markup SHA-256 before: `d260f90821c86d679275165daea3e39ab810305e214f662875bd7c97735f9826`
- Markup SHA-256 after: `26bb73b98565c9cd36e13369a3bbc1de9b7e80c03e867ccdcf64ac48aae989ad`
- Revision IDs: `714`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231957782384.reviewer-4-comment-4.item-07-atom-037.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ses 
~~~~

- After:

~~~~text
ses
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-038

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:58Z
- Author: Mike Li
- Markup SHA-256 before: `26bb73b98565c9cd36e13369a3bbc1de9b7e80c03e867ccdcf64ac48aae989ad`
- Markup SHA-256 after: `eaf960dc2992738772c024b4e68b45c693d8a1cf4bdab1a1fc2baf2ba4065be5`
- Revision IDs: `441`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231958436414.reviewer-4-comment-4.item-07-atom-038.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
classes
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "classes"
     - After: ""

### item-07-atom-039

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:19:58Z
- Author: Mike Li
- Markup SHA-256 before: `eaf960dc2992738772c024b4e68b45c693d8a1cf4bdab1a1fc2baf2ba4065be5`
- Markup SHA-256 after: `16b4a79f05b3b823a8678f8ec9c3ffdd9a7cbf0b2e20df7616dc9065f4f908cd`
- Revision IDs: `715`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231959143674.reviewer-4-comment-4.item-07-atom-039.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
nimum 
~~~~

- After:

~~~~text
nimum
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-040

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:19:59Z
- Author: Mike Li
- Markup SHA-256 before: `16b4a79f05b3b823a8678f8ec9c3ffdd9a7cbf0b2e20df7616dc9065f4f908cd`
- Markup SHA-256 after: `4ff81cd8fd5819983aec4443acfaa0741f9ce0c81a8eabde1b0eff6d0d43da52`
- Revision IDs: `443`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T231959811275.reviewer-4-comment-4.item-07-atom-040.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
minimum
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "minimum"
     - After: ""

### item-07-atom-041

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:00Z
- Author: Mike Li
- Markup SHA-256 before: `4ff81cd8fd5819983aec4443acfaa0741f9ce0c81a8eabde1b0eff6d0d43da52`
- Markup SHA-256 after: `85e861128a9073c2ecba648b1aefb803dfcadf33b782e0a9fd02e295fb9da774`
- Revision IDs: `716`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232000516720.reviewer-4-comment-4.item-07-atom-041.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
at 
~~~~

- After:

~~~~text
at
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-042

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:01Z
- Author: Mike Li
- Markup SHA-256 before: `85e861128a9073c2ecba648b1aefb803dfcadf33b782e0a9fd02e295fb9da774`
- Markup SHA-256 after: `08ea4d01ae6447b67f1a7ef75c02f0c22bdedfaf3cf88f0d98863f7bf99ac783`
- Revision IDs: `445`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232001215170.reviewer-4-comment-4.item-07-atom-042.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 at
~~~~

- After:

~~~~text
 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "at"
     - After: ""

### item-07-atom-043

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:01Z
- Author: Mike Li
- Markup SHA-256 before: `08ea4d01ae6447b67f1a7ef75c02f0c22bdedfaf3cf88f0d98863f7bf99ac783`
- Markup SHA-256 after: `2b02b810f746a7c8d8d7e961b3f03467d40b3ad0f57dc1df7825d214df6b0655`
- Revision IDs: `717`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232001891168.reviewer-4-comment-4.item-07-atom-043.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
res 
~~~~

- After:

~~~~text
res
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-044

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:02Z
- Author: Mike Li
- Markup SHA-256 before: `2b02b810f746a7c8d8d7e961b3f03467d40b3ad0f57dc1df7825d214df6b0655`
- Markup SHA-256 after: `dd073396d16817ea5db234c7cec88b6a56583402d6c934b6f3160a1ccf04f5d3`
- Revision IDs: `447`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232002550147.reviewer-4-comment-4.item-07-atom-044.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
closures
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "closures"
     - After: ""

### item-07-atom-045

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:03Z
- Author: Mike Li
- Markup SHA-256 before: `dd073396d16817ea5db234c7cec88b6a56583402d6c934b6f3160a1ccf04f5d3`
- Markup SHA-256 after: `72d9d34f096112d27d712cafe1ff92718812fac0a55e7744221ea0acc2473838`
- Revision IDs: `718`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232003222635.reviewer-4-comment-4.item-07-atom-045.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 147 
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " 147 "
     - After: ""

### item-07-atom-046

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:03Z
- Author: Mike Li
- Markup SHA-256 before: `72d9d34f096112d27d712cafe1ff92718812fac0a55e7744221ea0acc2473838`
- Markup SHA-256 after: `2c7b0b0657ca73ec5b1018425c5dbd660a6d153bac8fc60a219facd3d69c95e1`
- Revision IDs: `449`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232003920592.reviewer-4-comment-4.item-07-atom-046.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
and g
~~~~

- After:

~~~~text
 g
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "and"
     - After: ""

### item-07-atom-047

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:04Z
- Author: Mike Li
- Markup SHA-256 before: `2c7b0b0657ca73ec5b1018425c5dbd660a6d153bac8fc60a219facd3d69c95e1`
- Markup SHA-256 after: `845bcd24d965e3dcdd9a41628eaa6d525ceeae8dcf3fccea5a4b0730bbd62458`
- Revision IDs: `719`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232004624405.reviewer-4-comment-4.item-07-atom-047.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
9, 
~~~~

- After:

~~~~text
9,
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-048

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:05Z
- Author: Mike Li
- Markup SHA-256 before: `845bcd24d965e3dcdd9a41628eaa6d525ceeae8dcf3fccea5a4b0730bbd62458`
- Markup SHA-256 after: `cfd37d789c5e823d92d49218ee02967d9cf5cc31b5d9f7cf0757a514245bc6b1`
- Revision IDs: `451`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232005270331.reviewer-4-comment-4.item-07-atom-048.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
119,
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "119,"
     - After: ""

### item-07-atom-049

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:13Z
- Author: Mike Li
- Markup SHA-256 before: `cfd37d789c5e823d92d49218ee02967d9cf5cc31b5d9f7cf0757a514245bc6b1`
- Markup SHA-256 after: `b807116937916314bc85434e769c637e8681688635e00beb4bcdd0affafd87cc`
- Revision IDs: `720`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232013478352.reviewer-4-comment-4.item-07-atom-049.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
2, 
~~~~

- After:

~~~~text
2,
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-050

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:13Z
- Author: Mike Li
- Markup SHA-256 before: `b807116937916314bc85434e769c637e8681688635e00beb4bcdd0affafd87cc`
- Markup SHA-256 after: `ec7fe5879f319fea131f338264b448a74bc64a59c1aa03c4608fb5dfc0ab2094`
- Revision IDs: `453`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232014163542.reviewer-4-comment-4.item-07-atom-050.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
42,
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "42,"
     - After: ""

### item-07-atom-051

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:14Z
- Author: Mike Li
- Markup SHA-256 before: `ec7fe5879f319fea131f338264b448a74bc64a59c1aa03c4608fb5dfc0ab2094`
- Markup SHA-256 after: `53b321c335fc68e7bf288811f89f81c84eaf423cb3584398b39a483883ab2b44`
- Revision IDs: `721`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232014848591.reviewer-4-comment-4.item-07-atom-051.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ds 
~~~~

- After:

~~~~text
ds
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-052

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:15Z
- Author: Mike Li
- Markup SHA-256 before: `53b321c335fc68e7bf288811f89f81c84eaf423cb3584398b39a483883ab2b44`
- Markup SHA-256 after: `f2705ddf267751e945095e3101a65b351961809403f052fb622dba046396f4d9`
- Revision IDs: `455`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232015520119.reviewer-4-comment-4.item-07-atom-052.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
adds
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "adds"
     - After: ""

### item-07-atom-053

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:16Z
- Author: Mike Li
- Markup SHA-256 before: `f2705ddf267751e945095e3101a65b351961809403f052fb622dba046396f4d9`
- Markup SHA-256 after: `e73b1f9c0c455b79c0ac5c9b92229e1e3ab23d3a01108b29b6ac0eb2290a651a`
- Revision IDs: `722, 723`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232016208119.reviewer-4-comment-4.item-07-atom-053.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
matched groups, with maximum changes of 225 newly isolated people and 13,448 person-minutes. The broader road-closure rule 
~~~~

- After:

~~~~text
snapping
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "matched groups, with maximum changes of 225 newly isolated people and 13,448 person-minutes. The broader road-closure rule "
     - After: "snapping"

### item-07-atom-054

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:16Z
- Author: Mike Li
- Markup SHA-256 before: `e73b1f9c0c455b79c0ac5c9b92229e1e3ab23d3a01108b29b6ac0eb2290a651a`
- Markup SHA-256 after: `9874c766562e5df77a5985b91f3430855553f4a1c591e43adccdd5cde68cec68`
- Revision IDs: `724`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232016893646.reviewer-4-comment-4.item-07-atom-054.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
s in
~~~~

- After:

~~~~text
s
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " in"
     - After: ""

### item-07-atom-055

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:17Z
- Author: Mike Li
- Markup SHA-256 before: `9874c766562e5df77a5985b91f3430855553f4a1c591e43adccdd5cde68cec68`
- Markup SHA-256 after: `045669508e7dca81df6feeea38782ab9f08f253dd5e6ef61941df1122e877e6c`
- Revision IDs: `457`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232017568101.reviewer-4-comment-4.item-07-atom-055.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
aggregates a
~~~~

- After:

~~~~text
 a
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "aggregates"
     - After: ""

### item-07-atom-056

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:18Z
- Author: Mike Li
- Markup SHA-256 before: `045669508e7dca81df6feeea38782ab9f08f253dd5e6ef61941df1122e877e6c`
- Markup SHA-256 after: `48d0c7afd1bce3c067e0a5a39ddd1c9a3bf9d9711579d7d07ba514cf2ca59380`
- Revision IDs: `725`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232018259365.reviewer-4-comment-4.item-07-atom-056.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
g changes 
~~~~

- After:

~~~~text
g changes
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-07-atom-057

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:18Z
- Author: Mike Li
- Markup SHA-256 before: `48d0c7afd1bce3c067e0a5a39ddd1c9a3bf9d9711579d7d07ba514cf2ca59380`
- Markup SHA-256 after: `0acc3d752b4d88b92ac6c45d27b4d062200d34ec6111c3c9f204236c11c714dc`
- Revision IDs: `459`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232018985019.reviewer-4-comment-4.item-07-atom-057.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
g changes
~~~~

- After:

~~~~text
g 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "changes"
     - After: ""

### item-07-atom-058

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:19Z
- Author: Mike Li
- Markup SHA-256 before: `0acc3d752b4d88b92ac6c45d27b4d062200d34ec6111c3c9f204236c11c714dc`
- Markup SHA-256 after: `c641fdfe3b3e13ed1f9e6640f638b17c40be09743aa8c7dc908a5792edf60eb9`
- Revision IDs: `726`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232019682961.reviewer-4-comment-4.item-07-atom-058.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 changes delayed population by as much as 1,394 people. Settlement snapping 
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " changes delayed population by as much as 1,394 people. Settlement snapping "
     - After: ""

### item-07-atom-059

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:20Z
- Author: Mike Li
- Markup SHA-256 before: `c641fdfe3b3e13ed1f9e6640f638b17c40be09743aa8c7dc908a5792edf60eb9`
- Markup SHA-256 after: `ad439898486d79061b4f650913aa1024851f4655f29befece8244f56d52c6767`
- Revision IDs: `727`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232020383721.reviewer-4-comment-4.item-07-atom-059.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ps 
~~~~

- After:

~~~~text
ps, 
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: ","

### item-07-atom-060

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:20Z
- Author: Mike Li
- Markup SHA-256 before: `ad439898486d79061b4f650913aa1024851f4655f29befece8244f56d52c6767`
- Markup SHA-256 after: `1346da114b7565699593f8ba77968f7745ff470df3d517015c2df12a2eb3ece1`
- Revision IDs: `728`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232021122128.reviewer-4-comment-4.item-07-atom-060.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
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
96 facility-availability 
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "facility-availability "

### item-07-atom-061

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:21Z
- Author: Mike Li
- Markup SHA-256 before: `1346da114b7565699593f8ba77968f7745ff470df3d517015c2df12a2eb3ece1`
- Markup SHA-256 after: `fd60c3d762e03fea3b81f200cdcc7771b0f4effa676959392a01c6a4661301d0`
- Revision IDs: `729`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232021826266.reviewer-4-comment-4.item-07-atom-061.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 3
~~~~

- After:

~~~~text
 all 64 hazard-threshold groups, 3
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " all 64 hazard-threshold groups,"

### item-07-atom-062

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:22Z
- Author: Mike Li
- Markup SHA-256 before: `fd60c3d762e03fea3b81f200cdcc7771b0f4effa676959392a01c6a4661301d0`
- Markup SHA-256 after: `fd1fb4efd2349641fe9f82d4c03fd3e6d3372348877798388fe202d983d69218`
- Revision IDs: `461`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232022479729.reviewer-4-comment-4.item-07-atom-062.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
aggregate-active
~~~~

- After:

~~~~text
give 1,436,464 person-minutes and retain nine primary top-ten members, with Pajung replacing Gerkhu. At reference speeds, the populations delayed by more than 2, 5, and 10 minutes are 38,418, 34,260, and 21,644, respectively. Restricting destinations to clinical care raises newly isolated population to 17,798 and gives 33,260 people delayed by more than five minutes, with 607 baseline-eligible settlements rather than 610. The common baseline cohort contains 607 settlements and 532,296 people; its clinical-only comparison still adds 19 newly isolated settlements. Removing directly class-3-exposed destination records leaves the settlement access vectors unchanged within all 12 destination-by-speed comparisons. Paired structural comparisons show aggregate activity
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "aggregate-active"
     - After: "give 1,436,464 person-minutes and retain nine primary top-ten members, with Pajung replacing Gerkhu. At reference speeds, the populations delayed by more than 2, 5, and 10 minutes are 38,418, 34,260, and 21,644, respectively. Restricting destinations to clinical care raises newly isolated population to 17,798 and gives 33,260 people delayed by more than five minutes, with 607 baseline-eligible settlements rather than 610. The common baseline cohort contains 607 settlements and 532,296 people; its clinical-only comparison still adds 19 newly isolated settlements. Removing directly class-3-exposed destination records leaves the settlement access vectors unchanged within all 12 destination-by-speed comparisons. Paired structural comparisons show aggregate activity"

### item-07-atom-063

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:22Z
- Author: Mike Li
- Markup SHA-256 before: `fd1fb4efd2349641fe9f82d4c03fd3e6d3372348877798388fe202d983d69218`
- Markup SHA-256 after: `23ec133bdaf90c42bfa3c5c76790a0f0846a0a1d4a702acc70dbff08f1ed3897`
- Revision IDs: `730, 731`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232023154577.reviewer-4-comment-4.item-07-atom-063.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
is 
~~~~

- After:

~~~~text
speeds 
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "is"
     - After: "speeds"

### item-07-atom-064

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:23Z
- Author: Mike Li
- Markup SHA-256 before: `23ec133bdaf90c42bfa3c5c76790a0f0846a0a1d4a702acc70dbff08f1ed3897`
- Markup SHA-256 after: `dd0cc07e621e3bef7756b00e3d80c77114ab938ef8fe7e3fa4e5014c3878e6a3`
- Revision IDs: `732, 733`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232023828853.reviewer-4-comment-4.item-07-atom-064.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 availability
~~~~

- After:

~~~~text
 slower
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "availability"
     - After: "slower"

### item-07-atom-065

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:24Z
- Author: Mike Li
- Markup SHA-256 before: `dd0cc07e621e3bef7756b00e3d80c77114ab938ef8fe7e3fa4e5014c3878e6a3`
- Markup SHA-256 after: `ae0654a660f8cecbc56483cddd29c9ec3906df14b17e773f85adec50b204e053`
- Revision IDs: `734, 735`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232024516479.reviewer-4-comment-4.item-07-atom-065.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Facility
~~~~

- After:

~~~~text
Differential
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Facility"
     - After: "Differential"

### item-07-atom-066

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:25Z
- Author: Mike Li
- Markup SHA-256 before: `ae0654a660f8cecbc56483cddd29c9ec3906df14b17e773f85adec50b204e053`
- Markup SHA-256 after: `ee10104e55f59ef87c1a724e8a7009d56fa6773d782c702e7b23eb410ec45527`
- Revision IDs: `736`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232025178631.reviewer-4-comment-4.item-07-atom-066.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
n.
~~~~

- After:

~~~~text
n remains 13,906.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " remains 13,906"

### item-07-atom-067

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:25Z
- Author: Mike Li
- Markup SHA-256 before: `ee10104e55f59ef87c1a724e8a7009d56fa6773d782c702e7b23eb410ec45527`
- Markup SHA-256 after: `3517307bbc54040eb63f79febd5c3e094bc2c8a1b1eaf8a7fb36bec08539bf38`
- Revision IDs: `737, 738`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232025858056.reviewer-4-comment-4.item-07-atom-067.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
no change in the
~~~~

- After:

~~~~text
while
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "no change in the"
     - After: "while"

### item-07-atom-068

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:26Z
- Author: Mike Li
- Markup SHA-256 before: `3517307bbc54040eb63f79febd5c3e094bc2c8a1b1eaf8a7fb36bec08539bf38`
- Markup SHA-256 after: `70a9a6d62ef651a5d99b7b17a7527dc26370bea24d6021cc941ce021b37b67d2`
- Revision IDs: `739, 740`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232026534395.reviewer-4-comment-4.item-07-atom-068.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
but
~~~~

- After:

~~~~text
respectively,
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "but"
     - After: "respectively,"

### item-07-atom-069

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:27Z
- Author: Mike Li
- Markup SHA-256 before: `70a9a6d62ef651a5d99b7b17a7527dc26370bea24d6021cc941ce021b37b67d2`
- Markup SHA-256 after: `d587d74db64046806f242bb5e212e095c9b248993c6567430797ea7750c391d4`
- Revision IDs: `741, 742`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232027221383.reviewer-4-comment-4.item-07-atom-069.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
426
~~~~

- After:

~~~~text
677
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "426"
     - After: "677"

### item-07-atom-070

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:27Z
- Author: Mike Li
- Markup SHA-256 before: `d587d74db64046806f242bb5e212e095c9b248993c6567430797ea7750c391d4`
- Markup SHA-256 after: `6ebe8b8448a0b39fe736586b53f9b69ab8c47e826a8b2bb1c2b65ad5cd73a9da`
- Revision IDs: `743, 744`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232027914384.reviewer-4-comment-4.item-07-atom-070.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
70
~~~~

- After:

~~~~text
609
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "70"
     - After: "609"

### item-07-atom-071

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:28Z
- Author: Mike Li
- Markup SHA-256 before: `6ebe8b8448a0b39fe736586b53f9b69ab8c47e826a8b2bb1c2b65ad5cd73a9da`
- Markup SHA-256 after: `e820f2431bac0b242c5f26301b9dc5c5f4f0eb494f3e3971b4d317da39042ed3`
- Revision IDs: `745, 746`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232028608081.reviewer-4-comment-4.item-07-atom-071.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
394 delayed people
~~~~

- After:

~~~~text
016,129
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "394 delayed people"
     - After: "016,129"

### item-07-atom-072

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:29Z
- Author: Mike Li
- Markup SHA-256 before: `e820f2431bac0b242c5f26301b9dc5c5f4f0eb494f3e3971b4d317da39042ed3`
- Markup SHA-256 after: `d88a330138907445b409fa1ea1f04d3b7aa524a133707f2cce52a83037f089c4`
- Revision IDs: `747`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232029307710.reviewer-4-comment-4.item-07-atom-072.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
access outcomes across all 64 matched groups, with maximum changes of
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "access outcomes across all 64 matched groups, with maximum changes of"
     - After: ""

### item-07-atom-073

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-05
- Timestamp: 2026-10-23T14:20:29Z
- Author: Mike Li
- Markup SHA-256 before: `d88a330138907445b409fa1ea1f04d3b7aa524a133707f2cce52a83037f089c4`
- Markup SHA-256 after: `466d465754e2293244ba46eafb9bfcd3d3e24269942ba721ddcda16ba49a7a04`
- Revision IDs: `462`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232030124960.reviewer-4-comment-4.item-07-atom-073.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
s aggregate 
~~~~

- After:

~~~~text
s 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "aggregate "
     - After: ""

### item-07-atom-074

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:30Z
- Author: Mike Li
- Markup SHA-256 before: `466d465754e2293244ba46eafb9bfcd3d3e24269942ba721ddcda16ba49a7a04`
- Markup SHA-256 after: `1d61112b1513ffed1ff8b744e260441fb888c4005ab5d827319e504a62678273`
- Revision IDs: `748, 749`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232030812644.reviewer-4-comment-4.item-07-atom-074.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
the five structural factors. Changing the hazard threshold affects 
~~~~

- After:

~~~~text
give
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "the five structural factors. Changing the hazard threshold affects "
     - After: "give"

### item-07-atom-075

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:31Z
- Author: Mike Li
- Markup SHA-256 before: `1d61112b1513ffed1ff8b744e260441fb888c4005ab5d827319e504a62678273`
- Markup SHA-256 after: `1dcd88946d85304ac96bc0e6e620f6d070e6389b7a41dc8f542bb91c28d04326`
- Revision IDs: `750, 751`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232031513381.reviewer-4-comment-4.item-07-atom-075.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
for
~~~~

- After:

~~~~text
multipliers
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "for"
     - After: "multipliers"

### item-07-atom-076

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:32Z
- Author: Mike Li
- Markup SHA-256 before: `1dcd88946d85304ac96bc0e6e620f6d070e6389b7a41dc8f542bb91c28d04326`
- Markup SHA-256 after: `588e893e6f0600d06b127029869fa069209cec567cc0f876fe5c98968680c6bf`
- Revision IDs: `752, 753`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232032199780.reviewer-4-comment-4.item-07-atom-076.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
roles
~~~~

- After:

~~~~text
speed
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "roles"
     - After: "speed"

### item-07-atom-077

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:32Z
- Author: Mike Li
- Markup SHA-256 before: `588e893e6f0600d06b127029869fa069209cec567cc0f876fe5c98968680c6bf`
- Markup SHA-256 after: `d89ae3dc3b52b3af0f65956dfa6e253b3930ec2fc8d987e3aadd5208f8c91f1a`
- Revision IDs: `754, 755`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232032875938.reviewer-4-comment-4.item-07-atom-077.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
distinct
~~~~

- After:

~~~~text
1.25
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "distinct"
     - After: "1.25"

### item-07-atom-078

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:33Z
- Author: Mike Li
- Markup SHA-256 before: `d89ae3dc3b52b3af0f65956dfa6e253b3930ec2fc8d987e3aadd5208f8c91f1a`
- Markup SHA-256 after: `c72ed461df6260c5139c699e6ed6ce78d02e11341c533a53d4d1de47129031f7`
- Revision IDs: `756, 757`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232033555262.reviewer-4-comment-4.item-07-atom-078.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
reveal
~~~~

- After:

~~~~text
and
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "reveal"
     - After: "and"

### item-07-atom-079

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:34Z
- Author: Mike Li
- Markup SHA-256 before: `c72ed461df6260c5139c699e6ed6ce78d02e11341c533a53d4d1de47129031f7`
- Markup SHA-256 after: `5a92318bc979c8985bce5fa2b36c5241cce44bd0d084c382da9813014f403513`
- Revision IDs: `758, 759`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232034237515.reviewer-4-comment-4.item-07-atom-079.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
comparisons a
~~~~

- After:

~~~~text
0.75 a
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "comparisons"
     - After: "0.75"

### item-07-atom-080

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:34Z
- Author: Mike Li
- Markup SHA-256 before: `5a92318bc979c8985bce5fa2b36c5241cce44bd0d084c382da9813014f403513`
- Markup SHA-256 after: `e4066bcb3c7fbb546326421658163aabd43ab754b4775537eaf0d47d307511a4`
- Revision IDs: `760, 761`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232034920658.reviewer-4-comment-4.item-07-atom-080.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Paired 0
~~~~

- After:

~~~~text
Uniform 0
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Paired"
     - After: "Uniform"

### item-07-atom-081

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:35Z
- Author: Mike Li
- Markup SHA-256 before: `e4066bcb3c7fbb546326421658163aabd43ab754b4775537eaf0d47d307511a4`
- Markup SHA-256 after: `34be606b7cbeead5385966dc30e5dcdab217af52fb4a9b8d92a893f60d46e881`
- Revision IDs: `762, 763`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232035602751.reviewer-4-comment-4.item-07-atom-081.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
233
~~~~

- After:

~~~~text
097
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "233"
     - After: "097"

### item-07-atom-082

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:36Z
- Author: Mike Li
- Markup SHA-256 before: `34be606b7cbeead5385966dc30e5dcdab217af52fb4a9b8d92a893f60d46e881`
- Markup SHA-256 after: `d6309b42d687efef2917353f946273cdab25e121589124a123870b70c29e7921`
- Revision IDs: `764, 765`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232036290400.reviewer-4-comment-4.item-07-atom-082.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
540
~~~~

- After:

~~~~text
762
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "540"
     - After: "762"

### item-07-atom-083

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:36Z
- Author: Mike Li
- Markup SHA-256 before: `d6309b42d687efef2917353f946273cdab25e121589124a123870b70c29e7921`
- Markup SHA-256 after: `005f2a84b701ad3d109a0df45508224d8a0a320df36fceca73d8a326022984f4`
- Revision IDs: `766, 767`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232036972002.reviewer-4-comment-4.item-07-atom-083.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
488
~~~~

- After:

~~~~text
260
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "488"
     - After: "260"

### item-07-atom-084

- Location: Approved item 7/24: KE03 / Results / Network Disruption and Service-Access Loss / sensitivity paragraph
- Reason: 以验证后的速度、阈值、目的地和可用性对比直接回答本条，保留因子审计的主要结论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:37Z
- Author: Mike Li
- Markup SHA-256 before: `005f2a84b701ad3d109a0df45508224d8a0a320df36fceca73d8a326022984f4`
- Markup SHA-256 after: `eb785819d62e9c76bc5040d2728c74898b2961e5d5cb05bd3bc74fb0b1934972`
- Revision IDs: `768, 769`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232037642565.reviewer-4-comment-4.item-07-atom-084.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
24
~~~~

- After:

~~~~text
34
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "24"
     - After: "34"

### item-08

- Location: Approved item 8/24: KE03 / Results / Pre-Disaster Vulnerability Context / contextual rank changes
- Reason: 沿用既有contextual规则对新主排序的局部数值同步；不宣称完成EB审计。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:20:59Z
- Author: Mike Li
- Markup SHA-256 before: `eb785819d62e9c76bc5040d2728c74898b2961e5d5cb05bd3bc74fb0b1934972`
- Markup SHA-256 after: `dab4f556ced47b7fa3eebd8e752216e66d6f7b574e6930f1ef7d6553c8f7b715`
- Revision IDs: `770, 771`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232059947667.reviewer-4-comment-4.item-08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The survey evidence provides a limited contextual sensitivity at its supported reporting domains. District deprivation estimates span 12.5–37.5% for economic deprivation, 12.5–19.1% for basic-needs inadequacy, and 11.5–16.2% for public-service deprivation. Rasuwa is represented by a single primary sampling unit, so its point estimates lack a design-based confidence interval, whereas the historical shock records cover Dhading and Nuwakot. At the broader ecological-belt scale, pre-warning deficits range from 96.1% to 98.1% and risk-reduction participation deficits from 75.3% to 86.0%. Conditional on no preparation, variation varies more widely, although the mountain estimate has an effective sample size of four. In the Appendix sensitivity, Devighat and Bhainse remain first and second, Naubisephat and Betrawati exchange third and fourth place, and Timure moves from sixth to eighth. Each within-district settlement receives the same contextual value, so these movements identify dependence on the area-level adjustment. The primary score continues to represent hazard, population, and accessibility, while Appendix Figure A1 and Appendix Table A2 provide the complete contextual estimates and reliability labels.
~~~~

- After:

~~~~text
The survey evidence provides a limited contextual sensitivity at its supported reporting domains. District deprivation estimates span 12.5–37.5% for economic deprivation, 12.5–19.1% for basic-needs inadequacy, and 11.5–16.2% for public-service deprivation. Rasuwa is represented by a single primary sampling unit, so its point estimates lack a design-based confidence interval, whereas the historical shock records cover Dhading and Nuwakot. At the broader ecological-belt scale, pre-warning deficits range from 96.1% to 98.1% and risk-reduction participation deficits from 75.3% to 86.0%. Conditional on no preparation, variation varies more widely, although the mountain estimate has an effective sample size of four. In the Appendix sensitivity, Devighat and Bhainse remain first and second, Naubisephat and Betrawati exchange third and fourth place, and Timure moves from sixth to seventh. Each within-district settlement receives the same contextual value, so these movements identify dependence on the area-level adjustment. The primary score continues to represent hazard, population, and accessibility, while Appendix Figure A1 and Appendix Table A2 provide the complete contextual estimates and reliability labels.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "eighth"
     - After: "seventh"

### item-09-atom-001

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:00Z
- Author: Mike Li
- Markup SHA-256 before: `dab4f556ced47b7fa3eebd8e752216e66d6f7b574e6930f1ef7d6553c8f7b715`
- Markup SHA-256 after: `f0b803791b23f98e600224d62aea9bf970d3b81d5dc2bb8d6208eb1b78d247cd`
- Revision IDs: `772, 773`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232100848138.reviewer-4-comment-4.item-09-atom-001.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
36%
~~~~

- After:

~~~~text
31%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "36"
     - After: "31"

### item-09-atom-002

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:01Z
- Author: Mike Li
- Markup SHA-256 before: `f0b803791b23f98e600224d62aea9bf970d3b81d5dc2bb8d6208eb1b78d247cd`
- Markup SHA-256 after: `70444d0fe129b9d9ea435794fa6c02ae94d8a4f13d641b6529de0ea873dbdba0`
- Revision IDs: `774`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232101560989.reviewer-4-comment-4.item-09-atom-002.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 two
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " two"
     - After: ""

### item-09-atom-003

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:02Z
- Author: Mike Li
- Markup SHA-256 before: `70444d0fe129b9d9ea435794fa6c02ae94d8a4f13d641b6529de0ea873dbdba0`
- Markup SHA-256 after: `97407833d22c0d8b35d528b807a77487dec46ba442bc535c10a3ea731835c3f9`
- Revision IDs: `775, 776`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232102249797.reviewer-4-comment-4.item-09-atom-003.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
53
~~~~

- After:

~~~~text
47% and 37
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "53"
     - After: "47% and 37"

### item-09-atom-004

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:02Z
- Author: Mike Li
- Markup SHA-256 before: `97407833d22c0d8b35d528b807a77487dec46ba442bc535c10a3ea731835c3f9`
- Markup SHA-256 after: `1f4c478dbe59157e414e6e1e70f1d3ee705a7ebbba208932e848f510f71f0164`
- Revision IDs: `777, 778`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232102913915.reviewer-4-comment-4.item-09-atom-004.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
67
~~~~

- After:

~~~~text
63
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "67"
     - After: "63"

### item-09-atom-005

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:03Z
- Author: Mike Li
- Markup SHA-256 before: `1f4c478dbe59157e414e6e1e70f1d3ee705a7ebbba208932e848f510f71f0164`
- Markup SHA-256 after: `ee258c661e0a511f451b5099531d0aa94f95963891d2abf905ee3c6236f0ce0e`
- Revision IDs: `259`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232103595861.reviewer-4-comment-4.item-09-atom-005.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 each persist
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " each persist"
     - After: ""

### item-09-atom-006

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:04Z
- Author: Mike Li
- Markup SHA-256 before: `ee258c661e0a511f451b5099531d0aa94f95963891d2abf905ee3c6236f0ce0e`
- Markup SHA-256 after: `705980043eb1e3021b93962ff24cbb0cbbe3d4238315602a1ddc872b89137341`
- Revision IDs: `779, 780`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232104290288.reviewer-4-comment-4.item-09-atom-006.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Gerkhu, and the tenth-ranked unnamed settlement
~~~~

- After:

~~~~text
persists
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Gerkhu, and the tenth-ranked unnamed settlement"
     - After: "persists"

### item-09-atom-007

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:04Z
- Author: Mike Li
- Markup SHA-256 before: `705980043eb1e3021b93962ff24cbb0cbbe3d4238315602a1ddc872b89137341`
- Markup SHA-256 after: `685a46c49fb79084dac2556d7016df770f5bd0e63c158cc69693056d33f5eb0e`
- Revision IDs: `781`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232104983921.reviewer-4-comment-4.item-09-atom-007.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
i, p
~~~~

- After:

~~~~text
i p
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: ","
     - After: ""

### item-09-atom-008

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:05Z
- Author: Mike Li
- Markup SHA-256 before: `685a46c49fb79084dac2556d7016df770f5bd0e63c158cc69693056d33f5eb0e`
- Markup SHA-256 after: `48837c0506e8d2e6c036ff931804455d27c27428570540e137663ad9916ba8ce`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232105687418.reviewer-4-comment-4.item-09-atom-008.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
while the other thresholds retain all ten
~~~~

- After:

~~~~text
respectively
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "while the other thresholds retain all ten"
     - After: "respectively"

### item-09-atom-009

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:06Z
- Author: Mike Li
- Markup SHA-256 before: `48837c0506e8d2e6c036ff931804455d27c27428570540e137663ad9916ba8ce`
- Markup SHA-256 after: `62605281cb6a5f8bfbef6f0a12d7e9dd441e70a96e15232cb08486176de8f3d9`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232106385427.reviewer-4-comment-4.item-09-atom-009.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
s seven
~~~~

- After:

~~~~text
s nine, nine, and ten
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "seven"
     - After: "nine, nine, and ten"

### item-09-atom-010

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:06Z
- Author: Mike Li
- Markup SHA-256 before: `62605281cb6a5f8bfbef6f0a12d7e9dd441e70a96e15232cb08486176de8f3d9`
- Markup SHA-256 after: `9374ad14d082074f14a4a49e21bd1f4408777b540d7ad95afcfff8228870ec35`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232107074847.reviewer-4-comment-4.item-09-atom-010.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
n retains
~~~~

- After:

~~~~text
n eight,
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "retains"
     - After: "eight,"

### item-09-atom-011

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:07Z
- Author: Mike Li
- Markup SHA-256 before: `9374ad14d082074f14a4a49e21bd1f4408777b540d7ad95afcfff8228870ec35`
- Markup SHA-256 after: `7c88204b03b17e62d5da6d608c2fb151185fd755ee1373c95f8aba2fc020e537`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232107756415.reviewer-4-comment-4.item-09-atom-011.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
allocation e
~~~~

- After:

~~~~text
retain e
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "allocation"
     - After: "retain"

### item-09-atom-012

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:08Z
- Author: Mike Li
- Markup SHA-256 before: `7c88204b03b17e62d5da6d608c2fb151185fd755ee1373c95f8aba2fc020e537`
- Markup SHA-256 after: `4c5113b12a725c37f3908201a3d4e5783e04067ee985c40cbd4564b5d4b5b2cd`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232108426904.reviewer-4-comment-4.item-09-atom-012.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 m 
~~~~

- After:

~~~~text
 thresholds 
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "m"
     - After: "thresholds"

### item-09-atom-013

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:08Z
- Author: Mike Li
- Markup SHA-256 before: `4c5113b12a725c37f3908201a3d4e5783e04067ee985c40cbd4564b5d4b5b2cd`
- Markup SHA-256 after: `9db72acbd4df9d036caa9be9f4156e5d9e1141c5620e67b7bf1503f442b1785c`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232109125681.reviewer-4-comment-4.item-09-atom-013.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
500 t
~~~~

- After:

~~~~text
four t
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "500"
     - After: "four"

### item-09-atom-014

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:09Z
- Author: Mike Li
- Markup SHA-256 before: `9db72acbd4df9d036caa9be9f4156e5d9e1141c5620e67b7bf1503f442b1785c`
- Markup SHA-256 after: `4b051e83939e3e66b536ed49c16800b4c6535eb89e0ac95dfaf3685c8eee5349`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232109824899.reviewer-4-comment-4.item-09-atom-014.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
84
~~~~

- After:

~~~~text
89
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "84"
     - After: "89"

### item-09-atom-015

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:10Z
- Author: Mike Li
- Markup SHA-256 before: `4b051e83939e3e66b536ed49c16800b4c6535eb89e0ac95dfaf3685c8eee5349`
- Markup SHA-256 after: `1f4176052b37f2d893419558618ca4223c138255a044ede7ed29ad51db7b9902`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232110496609.reviewer-4-comment-4.item-09-atom-015.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
83
~~~~

- After:

~~~~text
88
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "83"
     - After: "88"

### item-09-atom-016

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:11Z
- Author: Mike Li
- Markup SHA-256 before: `1f4176052b37f2d893419558618ca4223c138255a044ede7ed29ad51db7b9902`
- Markup SHA-256 after: `aae95b9a6fbfff851bb064d72ea339bf754e3041c94208e2837074c3c9e1553f`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232111174461.reviewer-4-comment-4.item-09-atom-016.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
, 82
~~~~

- After:

~~~~text
, 87
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "82"
     - After: "87"

### item-09-atom-017

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:11Z
- Author: Mike Li
- Markup SHA-256 before: `aae95b9a6fbfff851bb064d72ea339bf754e3041c94208e2837074c3c9e1553f`
- Markup SHA-256 after: `2e1291819353fc9edcdd244ae0355f4d8dab25baa35820d3bc02bab80eeeaacd`
- Revision IDs: `261`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232111840378.reviewer-4-comment-4.item-09-atom-017.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
82
~~~~

- After:

~~~~text
87
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "82"
     - After: "87"

### item-09-atom-018

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:12Z
- Author: Mike Li
- Markup SHA-256 before: `2e1291819353fc9edcdd244ae0355f4d8dab25baa35820d3bc02bab80eeeaacd`
- Markup SHA-256 after: `9c4643b994efc18cacbc104a6d2c3c8d8c49a300007aba957c0eaccbe9ababcd`
- Revision IDs: `782, 783`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232112518602.reviewer-4-comment-4.item-09-atom-018.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ninth.
~~~~

- After:

~~~~text
eleventh.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "ninth"
     - After: "eleventh"

### item-09-atom-019

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:13Z
- Author: Mike Li
- Markup SHA-256 before: `9c4643b994efc18cacbc104a6d2c3c8d8c49a300007aba957c0eaccbe9ababcd`
- Markup SHA-256 after: `4fb62abd6e29509b19830d4f0618025be62bcc372fd68353215aac646577c8cb`
- Revision IDs: `784, 785`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232113196834.reviewer-4-comment-4.item-09-atom-019.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
seventh to e
~~~~

- After:

~~~~text
tenth to e
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "seventh"
     - After: "tenth"

### item-09-atom-020

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:13Z
- Author: Mike Li
- Markup SHA-256 before: `4fb62abd6e29509b19830d4f0618025be62bcc372fd68353215aac646577c8cb`
- Markup SHA-256 after: `4b5b0134fb96ba3f0c1d12d168cf3007dca27266a2df0da7c590260777506bdf`
- Revision IDs: `786`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232113894230.reviewer-4-comment-4.item-09-atom-020.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
hu 
~~~~

- After:

~~~~text
hu varies 
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "varies "

### item-09-atom-021

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:14Z
- Author: Mike Li
- Markup SHA-256 before: `4b5b0134fb96ba3f0c1d12d168cf3007dca27266a2df0da7c590260777506bdf`
- Markup SHA-256 after: `e9377361eeb8d0747a15d331cf37aaa021cc66d579baf92f93cd100b0365b89a`
- Revision IDs: `787, 788`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232114578904.reviewer-4-comment-4.item-09-atom-021.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
settlement f
~~~~

- After:

~~~~text
vary f
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "settlement"
     - After: "vary"

### item-09-atom-022

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:15Z
- Author: Mike Li
- Markup SHA-256 before: `e9377361eeb8d0747a15d331cf37aaa021cc66d579baf92f93cd100b0365b89a`
- Markup SHA-256 after: `377d7899f74f7ec5354aae46d245111e355668cd1156b2207129aa9786c33c6c`
- Revision IDs: `789, 790`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232115282686.reviewer-4-comment-4.item-09-atom-022.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Tarakeshwor
~~~~

- After:

~~~~text
settlements
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Tarakeshwor"
     - After: "settlements"

### item-09-atom-023

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:15Z
- Author: Mike Li
- Markup SHA-256 before: `377d7899f74f7ec5354aae46d245111e355668cd1156b2207129aa9786c33c6c`
- Markup SHA-256 after: `53f5e73a3fef15b2b7a00ad200bf8bed75a2c8315c3e0939f634fbf532abcc59`
- Revision IDs: `791, 792`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232115967576.reviewer-4-comment-4.item-09-atom-023.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
the u
~~~~

- After:

~~~~text
both u
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "the"
     - After: "both"

### item-09-atom-024

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:16Z
- Author: Mike Li
- Markup SHA-256 before: `53f5e73a3fef15b2b7a00ad200bf8bed75a2c8315c3e0939f634fbf532abcc59`
- Markup SHA-256 after: `0f351018597c655e6305d13d5a85c8f22ce1ef1f25cf6ad1e2aaf2c7e8f5ded2`
- Revision IDs: `793`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232116673550.reviewer-4-comment-4.item-09-atom-024.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
nth to ninth
~~~~

- After:

~~~~text
nth
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " to ninth"
     - After: ""

### item-09-atom-025

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:17Z
- Author: Mike Li
- Markup SHA-256 before: `0f351018597c655e6305d13d5a85c8f22ce1ef1f25cf6ad1e2aaf2c7e8f5ded2`
- Markup SHA-256 after: `661cf85e1cadf791ac8e17f286916c6c9344d94521a305cb38fa3eee1c7c2d85`
- Revision IDs: `794, 795`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232117378527.reviewer-4-comment-4.item-09-atom-025.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
i varies from
~~~~

- After:

~~~~text
i remains
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "varies from"
     - After: "remains"

### item-09-atom-026

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:17Z
- Author: Mike Li
- Markup SHA-256 before: `661cf85e1cadf791ac8e17f286916c6c9344d94521a305cb38fa3eee1c7c2d85`
- Markup SHA-256 after: `eb0ef1e4d38e0fa5ca98c5a56af797c4a683fee33ca7243780cddc6927e91cd2`
- Revision IDs: `796, 797`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232118080733.reviewer-4-comment-4.item-09-atom-026.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
99
~~~~

- After:

~~~~text
98
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "99"
     - After: "98"

### item-09-atom-027

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:18Z
- Author: Mike Li
- Markup SHA-256 before: `eb0ef1e4d38e0fa5ca98c5a56af797c4a683fee33ca7243780cddc6927e91cd2`
- Markup SHA-256 after: `78e6ad3b67fa30baa9cf025db780058bfbfd153e8d59d8e9c9e660d4122a6b1d`
- Revision IDs: `798, 799`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232118765609.reviewer-4-comment-4.item-09-atom-027.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
904
~~~~

- After:

~~~~text
902
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "904"
     - After: "902"

### item-09-atom-028

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:19Z
- Author: Mike Li
- Markup SHA-256 before: `78e6ad3b67fa30baa9cf025db780058bfbfd153e8d59d8e9c9e660d4122a6b1d`
- Markup SHA-256 after: `93577c41174fc6ad47c51801deb9b7294f44c757dd99186549f490b1e9c8944a`
- Revision IDs: `800, 801`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232119457602.reviewer-4-comment-4.item-09-atom-028.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
920
~~~~

- After:

~~~~text
917
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "920"
     - After: "917"

### item-09-atom-029

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:19Z
- Author: Mike Li
- Markup SHA-256 before: `93577c41174fc6ad47c51801deb9b7294f44c757dd99186549f490b1e9c8944a`
- Markup SHA-256 after: `fd1c7d9ee78a043cd007498d5419a6f51f27a4abfb589810cb7abae977377644`
- Revision IDs: `802, 803`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232120139313.reviewer-4-comment-4.item-09-atom-029.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
936
~~~~

- After:

~~~~text
932
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "936"
     - After: "932"

### item-09-atom-030

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:20Z
- Author: Mike Li
- Markup SHA-256 before: `fd1c7d9ee78a043cd007498d5419a6f51f27a4abfb589810cb7abae977377644`
- Markup SHA-256 after: `5a2079f6b494f3e1a20eb08be63b51f7ce4f44abf13a439db9deed1136365f59`
- Revision IDs: `804, 805`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232120845435.reviewer-4-comment-4.item-09-atom-030.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
940
~~~~

- After:

~~~~text
936
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "940"
     - After: "936"

### item-09-atom-031

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:21Z
- Author: Mike Li
- Markup SHA-256 before: `5a2079f6b494f3e1a20eb08be63b51f7ce4f44abf13a439db9deed1136365f59`
- Markup SHA-256 after: `a9c1795f59a209bc5efd42b78cccf276e8d8cd8a9188877f20d043102336ecbb`
- Revision IDs: `806, 807`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232121544495.reviewer-4-comment-4.item-09-atom-031.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
948
~~~~

- After:

~~~~text
943
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "948"
     - After: "943"

### item-09-atom-032

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:22Z
- Author: Mike Li
- Markup SHA-256 before: `a9c1795f59a209bc5efd42b78cccf276e8d8cd8a9188877f20d043102336ecbb`
- Markup SHA-256 after: `78d565f877d7e3a95f22b6844486ef4c5ea180e8cbeebe568c2425e21c445a24`
- Revision IDs: `259`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232122210184.reviewer-4-comment-4.item-09-atom-032.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
three of four
~~~~

- After:

~~~~text
three of four allocations and Gerkhu in one, while the other primary top-ten settlements persist in all four
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " allocations and Gerkhu in one, while the other primary top-ten settlements persist in all four"

### item-09-atom-033

- Location: Approved item 9/24: KE03 / Results / Settlement Intervention Priorities / paragraph beginning Table 2 identifies
- Reason: 逐项对齐新Table2分数、结构区间、四分配阈值和10007权重规格；保留仍有效的解释及段落顺序。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-3#part-04
- Timestamp: 2026-10-23T14:21:22Z
- Author: Mike Li
- Markup SHA-256 before: `78d565f877d7e3a95f22b6844486ef4c5ea180e8cbeebe568c2425e21c445a24`
- Markup SHA-256 after: `786dc213bb36cf81e65e4b88658c2cdebde3904915ce1f0912a2702dac94069d`
- Revision IDs: `259`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232122894202.reviewer-4-comment-4.item-09-atom-033.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
all four allocations
~~~~

- After:

~~~~text
all four
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " allocations"
     - After: ""

### item-10-atom-001

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:34Z
- Author: Mike Li
- Markup SHA-256 before: `786dc213bb36cf81e65e4b88658c2cdebde3904915ce1f0912a2702dac94069d`
- Markup SHA-256 after: `01640ed49e1675ae847a503032072df9d606961098fa582ce1a636715cc1f37e`
- Revision IDs: `808, 809`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232134321851.reviewer-4-comment-4.item-10-atom-001.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
a minimum of 36
~~~~

- After:

~~~~text
31
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "a minimum of 36"
     - After: "31"

### item-10-atom-002

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:34Z
- Author: Mike Li
- Markup SHA-256 before: `01640ed49e1675ae847a503032072df9d606961098fa582ce1a636715cc1f37e`
- Markup SHA-256 after: `c250415054c2c1d66677b83b65f9a9e6ad3d9747f0af02bfe851566630974e66`
- Revision IDs: `810, 811`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232135011435.reviewer-4-comment-4.item-10-atom-002.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
three boundary settlements
~~~~

- After:

~~~~text
Gerkhu
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "three boundary settlements"
     - After: "Gerkhu"

### item-10-atom-003

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:35Z
- Author: Mike Li
- Markup SHA-256 before: `c250415054c2c1d66677b83b65f9a9e6ad3d9747f0af02bfe851566630974e66`
- Markup SHA-256 after: `b96a7da600653af2b4afeaefd6ee57f9df8f5f950704c2b7781d575ca0822963`
- Revision IDs: `812, 813`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232135691181.reviewer-4-comment-4.item-10-atom-003.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Gerkhu. Allocation persistence falls to 75
~~~~

- After:

~~~~text
25
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Gerkhu. Allocation persistence falls to 75"
     - After: "25"

### item-10-atom-004

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:36Z
- Author: Mike Li
- Markup SHA-256 before: `b96a7da600653af2b4afeaefd6ee57f9df8f5f950704c2b7781d575ca0822963`
- Markup SHA-256 after: `b600a9ef18303e6980cf6949a1fd573ec80ef6f946a2fb46ec992a88f52043d0`
- Revision IDs: `814`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232136392598.reviewer-4-comment-4.item-10-atom-004.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
–9
~~~~

- After:

~~~~text
–9 for the two unnamed settlements and 10–11 for Gerkhu. Allocation persistence is 75%
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " for the two unnamed settlements and 10–11 for Gerkhu. Allocation persistence is 75%"

### item-10-atom-005

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:36Z
- Author: Mike Li
- Markup SHA-256 before: `b600a9ef18303e6980cf6949a1fd573ec80ef6f946a2fb46ec992a88f52043d0`
- Markup SHA-256 after: `622e8da5bd9e1c04685ce74b1c50af18171ccb670f8c97658868eb64407f164e`
- Revision IDs: `815, 816`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232137082878.reviewer-4-comment-4.item-10-atom-005.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
7–
~~~~

- After:

~~~~text
8–
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "7"
     - After: "8"

### item-10-atom-006

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:37Z
- Author: Mike Li
- Markup SHA-256 before: `622e8da5bd9e1c04685ce74b1c50af18171ccb670f8c97658868eb64407f164e`
- Markup SHA-256 after: `a41a6228a0cd8cdd112852d9604cc4c0355e90c056cab7b838647f78dbb214ac`
- Revision IDs: `817`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232137794301.reviewer-4-comment-4.item-10-atom-006.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ts,
~~~~

- After:

~~~~text
ts and at 7–7 for Rasuwa Gadhi,
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " and at 7–7 for Rasuwa Gadhi"

### item-10-atom-007

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:38Z
- Author: Mike Li
- Markup SHA-256 before: `a41a6228a0cd8cdd112852d9604cc4c0355e90c056cab7b838647f78dbb214ac`
- Markup SHA-256 after: `c7e2e2f93314a907c593fc3adae83ce6917a303c7e172f46d37adcab3954e9af`
- Revision IDs: `818, 819`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232138478340.reviewer-4-comment-4.item-10-atom-007.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
stability
~~~~

- After:

~~~~text
common top-ten members
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "stability"
     - After: "common top-ten members"

### item-10-atom-008

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:38Z
- Author: Mike Li
- Markup SHA-256 before: `c7e2e2f93314a907c593fc3adae83ce6917a303c7e172f46d37adcab3954e9af`
- Markup SHA-256 after: `4699d0039cd0423b2921cd7efa54338ffb8eb595d0038fb514d507f592c2871c`
- Revision IDs: `820, 821`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232139170050.reviewer-4-comment-4.item-10-atom-008.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
membership c
~~~~

- After:

~~~~text
nine c
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "membership"
     - After: "nine"

### item-10-atom-009

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:39Z
- Author: Mike Li
- Markup SHA-256 before: `4699d0039cd0423b2921cd7efa54338ffb8eb595d0038fb514d507f592c2871c`
- Markup SHA-256 after: `0bc23e4997c90f98aa3bc0437c5945412302b6b17217ba05e0ddfe960e9229a9`
- Revision IDs: `822, 823`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232139891593.reviewer-4-comment-4.item-10-atom-009.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
supports
~~~~

- After:

~~~~text
identifies
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "supports"
     - After: "identifies"

### item-10-atom-010

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:40Z
- Author: Mike Li
- Markup SHA-256 before: `0bc23e4997c90f98aa3bc0437c5945412302b6b17217ba05e0ddfe960e9229a9`
- Markup SHA-256 after: `b8d708c2cf499fe7e8b9728aa7efc7a5fc574c91d72c67092f69f2f52b1d2f39`
- Revision IDs: `824`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232140609067.reviewer-4-comment-4.item-10-atom-010.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
;
~~~~

- After:

~~~~text
 in 32 groups;
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " in 32 groups"

### item-10-atom-011

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-06
- Timestamp: 2026-10-23T14:21:41Z
- Author: Mike Li
- Markup SHA-256 before: `b8d708c2cf499fe7e8b9728aa7efc7a5fc574c91d72c67092f69f2f52b1d2f39`
- Markup SHA-256 after: `25fc44063d1f8fa8a50bf373d3ec8ded833ea16434c31575a25df4d6fc3fd88c`
- Revision IDs: `490`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232141281782.reviewer-4-comment-4.item-10-atom-011.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
changing to
~~~~

- After:

~~~~text
changes to
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "changing"
     - After: "changes"

### item-10-atom-012

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-06
- Timestamp: 2026-10-23T14:21:41Z
- Author: Mike Li
- Markup SHA-256 before: `25fc44063d1f8fa8a50bf373d3ec8ded833ea16434c31575a25df4d6fc3fd88c`
- Markup SHA-256 after: `f644500bd7bb7b003ff0c5d79e35f31ad49d4227ebea28d7eeefa630e7c3bca8`
- Revision IDs: `492`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232141960090.reviewer-4-comment-4.item-10-atom-012.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
without change
~~~~

- After:

~~~~text
and change
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "without"
     - After: "and"

### item-10-atom-013

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:42Z
- Author: Mike Li
- Markup SHA-256 before: `f644500bd7bb7b003ff0c5d79e35f31ad49d4227ebea28d7eeefa630e7c3bca8`
- Markup SHA-256 after: `64e16b8423d6bdde3f74e8de7b61784e41c364dcbf94ed849f75423a145e9b36`
- Revision IDs: `825, 826`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232142652340.reviewer-4-comment-4.item-10-atom-013.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
32 of 6
~~~~

- After:

~~~~text
all 6
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "32 of"
     - After: "all"

### item-10-atom-014

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:43Z
- Author: Mike Li
- Markup SHA-256 before: `64e16b8423d6bdde3f74e8de7b61784e41c364dcbf94ed849f75423a145e9b36`
- Markup SHA-256 after: `806799b1d749323f73ac140021ad3e692a4639ae69c4824aaa97993903b00502`
- Revision IDs: `827, 828`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232143348040.reviewer-4-comment-4.item-10-atom-014.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
three
~~~~

- After:

~~~~text
Gerkhu and Lingling alternate at the membership boundary; two membership sets and four
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "three"
     - After: "Gerkhu and Lingling alternate at the membership boundary; two membership sets and four"

### item-10-atom-015

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-06
- Timestamp: 2026-10-23T14:21:43Z
- Author: Mike Li
- Markup SHA-256 before: `806799b1d749323f73ac140021ad3e692a4639ae69c4824aaa97993903b00502`
- Markup SHA-256 after: `7c473775c252f567c92137f79bfd8288019e23e6005af4d2b1f72d4806527c79`
- Revision IDs: `498`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232144026268.reviewer-4-comment-4.item-10-atom-015.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
invariant
~~~~

- After:

~~~~text
belong to the top ten
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "invariant"
     - After: "belong to the top ten"

### item-10-atom-016

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-06
- Timestamp: 2026-10-23T14:21:44Z
- Author: Mike Li
- Markup SHA-256 before: `7c473775c252f567c92137f79bfd8288019e23e6005af4d2b1f72d4806527c79`
- Markup SHA-256 after: `2d0bc181516b4c89f90bc0f396c94d6db5d48e40efecbe47157caebc7d162a02`
- Revision IDs: `500`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232144701557.reviewer-4-comment-4.item-10-atom-016.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
p is
~~~~

- After:

~~~~text
p always
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "is"
     - After: "always"

### item-10-atom-017

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-06
- Timestamp: 2026-10-23T14:21:45Z
- Author: Mike Li
- Markup SHA-256 before: `2d0bc181516b4c89f90bc0f396c94d6db5d48e40efecbe47157caebc7d162a02`
- Markup SHA-256 after: `6415b97e58621b139c7c0c693920d1e93c278db1fe398dfb07a33645a345c23a`
- Revision IDs: `502`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232145386134.reviewer-4-comment-4.item-10-atom-017.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
membership a
~~~~

- After:

~~~~text
settlements a
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "membership"
     - After: "settlements"

### item-10-atom-018

- Location: Approved item 10/24: KE03 / Results / Priority Robustness
- Reason: 撤回旧定义下的成员完全不变结论，准确区分成员/顺序及三类敏感性，不合并分母。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:21:45Z
- Author: Mike Li
- Markup SHA-256 before: `6415b97e58621b139c7c0c693920d1e93c278db1fe398dfb07a33645a345c23a`
- Markup SHA-256 after: `7684a41ecf7685abe0dec523d38f9cd89c2a84cadf030e687eabf4a15b4dcf03`
- Revision IDs: `829, 830`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232146071548.reviewer-4-comment-4.item-10-atom-018.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
, top-ten
~~~~

- After:

~~~~text
, nine
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "top-ten"
     - After: "nine"

### item-11

- Location: Approved item 11/24: KE03 / Results / Road-Repair Screening and Portfolio Benefits / single-section benefits
- Reason: 更新有限改善总量和逐点收益层验证的14聚落/4415人；重连收益及候选身份不变。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:03Z
- Author: Mike Li
- Markup SHA-256 before: `7684a41ecf7685abe0dec523d38f9cd89c2a84cadf030e687eabf4a15b4dcf03`
- Markup SHA-256 after: `e7536d981bda6e7bd55bbbf4c00ecd9545c762ee09f9cda04741b88a59cb5eec`
- Revision IDs: `831, 832, 833, 834, 835`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232203298080.reviewer-4-comment-4.item-11.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The two positive single-section candidates supply different types of access benefit. Reopening the screened Pasang Lhamu Highway section restores one settlement and reconnects 2,678 assigned people. Its modeled benefit is concentrated in reconnection, with no additional person-minute gain among settlements that already retain a finite path. Reopening the second, unnamed road section reconnects no isolated settlement but reduces finite delay by 121,986 person-minutes. Figure 4 maps both sections and displays their marginal contributions. Their spatial separation corresponds to different graph roles: the highway section restores a disconnected route, while the second section shortens paths that remain connected. Among 194 screened candidates, these are the only two sections with a positive primary-scenario access benefit. The screening tuple ranks reconnection first, finite improvement second, and modeled reopened length third. Engineering feasibility, construction inputs, traffic function, and local use form the subsequent decision stage, where benefit type can be compared with repair time, safety, resource demand, and strategic road function for each candidate section.
~~~~

- After:

~~~~text
The two positive single-section candidates supply different types of access benefit. Reopening the screened Pasang Lhamu Highway section restores one settlement and reconnects 2,678 assigned people. Its modeled benefit is concentrated in reconnection, with no additional person-minute gain among settlements that already retain a finite path. Reopening the second, unnamed road section reconnects no isolated settlement but reduces finite delay by 55,087 person-minutes across 14 settlements with 4,415 assigned people. Figure 4 maps both sections and displays their marginal contributions. Their spatial separation corresponds to different graph roles: the highway section restores a disconnected route, while the second section shortens paths that remain connected. Among 194 screened candidates, these are the only two sections with a positive primary-scenario access benefit. The screening tuple ranks reconnection first, finite improvement second, and modeled reopened length third. Engineering feasibility, construction inputs, traffic function, and local use form the subsequent decision stage, where benefit type can be compared with repair time, safety, resource demand, and strategic road function for each candidate section.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"
  3. `insert`
     - Before: ""
     - After: " across 14 settlements with 4,415 assigned people"

### item-12

- Location: Approved item 12/24: KE03 / Results / Road-Repair Screening and Portfolio Benefits / forward portfolios
- Reason: 同步Table3并把平台限定在实际验证的前向序列；尚未完成成对互补分析，不保留“全部可用收益已耗尽”的推论。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:03Z
- Author: Mike Li
- Markup SHA-256 before: `e7536d981bda6e7bd55bbbf4c00ecd9545c762ee09f9cda04741b88a59cb5eec`
- Markup SHA-256 after: `80acd6111bfec65b81ab7c29d83fd7ee06684ba70dd85a1373e16c297fdc31ea`
- Revision IDs: `836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232203886747.reviewer-4-comment-4.item-12.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Joint rerouting captures all positive primary-scenario access benefit by portfolio size K=2. Table 3 shows that K=1 reconnects 2,678 people; adding the second section preserves that reconnection and supplies 121,986 person-minutes of finite improvement. Portfolios of three and five sections repeat the same two access outcomes, giving zero marginal reconnection and zero marginal finite improvement. The plateau occurs because the first two selections cover the complementary reconnection and delay-reduction functions available among screened candidates for the retained destinations. Joint rerouting confirms that the combined benefit is produced by the two-section set rather than by adding independent single-link totals. Each fixed portfolio produces a positive benefit in 67% of the nominal structural scenarios. Given the repeated aggregate profiles identified in the factor audit, this percentage describes scenario coverage rather than an engineering probability. The primary model therefore directs engineering assessment toward the two positive sections and treats the larger sets as redundancy checks when resources permit broader engineering and corridor-function inspection later.
~~~~

- After:

~~~~text
Along the evaluated forward sequence, primary-scenario access benefit reaches a plateau at portfolio size K=2. Table 3 shows that K=1 reconnects 2,678 people; adding the second section preserves that reconnection and supplies 55,087 person-minutes of finite improvement. Portfolios of three and five sections repeat the same two access outcomes, giving zero marginal reconnection and zero marginal finite improvement. The first two selections supply the reconnection and delay-reduction gains observed within this sequence for the retained destinations. Joint rerouting confirms that the combined benefit is produced by the two-section set rather than by adding independent single-link totals. Each fixed portfolio produces a positive benefit in 67% of the nominal structural scenarios. Given the repeated aggregate profiles identified in the factor audit, this percentage describes scenario coverage rather than an engineering probability. The primary model therefore directs engineering assessment toward the two positive sections and treats the larger sets as redundancy checks when resources permit broader engineering and corridor-function inspection later.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Joint"
     - After: "Along"
  2. `replace`
     - Before: "rerouting"
     - After: "the"
  3. `replace`
     - Before: "captures"
     - After: "evaluated"
  4. `replace`
     - Before: "all"
     - After: "forward"
  5. `replace`
     - Before: "positive"
     - After: "sequence,"
  6. `replace`
     - Before: "by"
     - After: "reaches a plateau at"
  7. `replace`
     - Before: "121"
     - After: "55"
  8. `replace`
     - Before: "986"
     - After: "087"
  9. `delete`
     - Before: "plateau occurs because the "
     - After: ""
  10. `replace`
     - Before: "cover"
     - After: "supply"
  11. `delete`
     - Before: " complementary"
     - After: ""
  12. `replace`
     - Before: "functions"
     - After: "gains"
  13. `replace`
     - Before: "available"
     - After: "observed"
  14. `replace`
     - Before: "among"
     - After: "within"
  15. `replace`
     - Before: "screened"
     - After: "this"
  16. `replace`
     - Before: "candidates"
     - After: "sequence"

### item-13

- Location: Approved item 13/24: KE03 / Discussion / Integrated Hazard, Accessibility, and Priority Findings
- Reason: 修正新权重结果中Betrawati并非严格100%的精度问题；不依赖表中整数四舍五入作全称判断。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:04Z
- Author: Mike Li
- Markup SHA-256 before: `80acd6111bfec65b81ab7c29d83fd7ee06684ba70dd85a1373e16c297fdc31ea`
- Markup SHA-256 after: `4e1c1d84aa2c953d5d37432bda02e2d56034838340308cf8c57636a98b1dc513`
- Revision IDs: `866, 867, 868, 869, 870`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232204413319.reviewer-4-comment-4.item-13.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The integrated evidence changes the decision picture produced by the physical footprint alone. Hazard classes establish the spatial confidence of the event corridor, assigned population locates represented human exposure, and network simulation separates finite delay from complete isolation. The highest-ranked settlements combine strength across all three components, with complete isolation distinguishing several northern communities and population elevating the leading Bidur-area settlements. Component maps and table columns make the source of every leading score visible. The robustness diagnostics then show whether a rank responds to the event-network representation, population linkage, or component weights. Devighat, Bhainse, Naubisephat, and Betrawati remain fixed across the tested structural states and persist under all allocation and weighting specifications. Lower positions move mainly under allocation and weighting choices. This contrast matters operationally because verification resources can first target the stable leading group and then investigate the population and preference assumptions responsible for the boundary ranks. The resulting queue therefore links rank position to a specific verification task rather than presenting all priorities as equally certain.
~~~~

- After:

~~~~text
The integrated evidence changes the decision picture produced by the physical footprint alone. Hazard classes establish the spatial confidence of the event corridor, assigned population locates represented human exposure, and network simulation separates finite delay from complete isolation. The highest-ranked settlements combine strength across all three components, with complete isolation distinguishing several northern communities and population elevating the leading Bidur-area settlements. Component maps and table columns make the source of every leading score visible. The robustness diagnostics then show whether a rank responds to the event-network representation, population linkage, or component weights. Devighat, Bhainse, Naubisephat, and Betrawati remain fixed across the tested structural states and persist under all allocation thresholds; weight-rule top-ten persistence is 100% for the first three and 99.85% for Betrawati. Lower positions move mainly under allocation and weighting choices. This contrast matters operationally because verification resources can first target the stable leading group and then investigate the population and preference assumptions responsible for the boundary ranks. The resulting queue therefore links rank position to a specific verification task rather than presenting all priorities as equally certain.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "thresholds; weight-rule top-ten persistence is 100% for the first three "
  2. `replace`
     - Before: "weighting"
     - After: "99.85%"
  3. `replace`
     - Before: "specifications"
     - After: "for Betrawati"

### item-14

- Location: Approved item 14/24: KE03 / Discussion / Implications for Emergency Access and Road Restoration
- Reason: 同步新主道路结果的证据范围；只陈述已核前向序列，不提前回答仍待分析的全局互补性。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:12Z
- Author: Mike Li
- Markup SHA-256 before: `4e1c1d84aa2c953d5d37432bda02e2d56034838340308cf8c57636a98b1dc513`
- Markup SHA-256 after: `41091449d56cf34f595c7de9284b6fc8ae697f44beda39b876848364ffc2c6f4`
- Revision IDs: `871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232212710635.reviewer-4-comment-4.item-14.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The road-restoration results favor portfolio-based screening because reconnection and finite-delay reduction arise from different links. Joint rerouting captures this complementarity by recalculating each candidate's value after previously selected sections reopen (Macea et al., 2026). The first two sections exhaust the positive benefit available for the retained destinations, and the plateau at larger portfolio sizes identifies redundancy in that access model. Transport-network studies similarly show that link criticality varies with network state and detour use (Nitheesh & Bhavathrathan, 2025; Sohn, 2006). Engineering assessment can now focus on the two positive candidates and collect data on structural condition, repair duration, cost, crew, materials, traffic, and construction safety. Those variables can convert the current access-benefit screen into a feasible sequence. They can also reveal whether a lower modeled-access candidate deserves earlier treatment because it is faster, safer, cheaper, or essential for freight and evacuation. In complex intercity systems, road functionality can amplify losses, making this second-stage assessment central to operational planning and to comparing access benefits with wider corridor functions for emergency logistics and recovery (Kilanitis & Sextos, 2019).
~~~~

- After:

~~~~text
The road-restoration results favor portfolio-based screening because reconnection and finite-delay reduction arise from different links. Joint rerouting captures this complementarity by recalculating each candidate's value after previously selected sections reopen (Macea et al., 2026). Along the evaluated forward sequence, the first two selections supply the benefits shown in Figure 4, with no additional gain at K=3 or K=5. Transport-network studies similarly show that link criticality varies with network state and detour use (Nitheesh & Bhavathrathan, 2025; Sohn, 2006). Engineering assessment can now focus on the two positive candidates and collect data on structural condition, repair duration, cost, crew, materials, traffic, and construction safety. Those variables can convert the current access-benefit screen into a feasible sequence. They can also reveal whether a lower modeled-access candidate deserves earlier treatment because it is faster, safer, cheaper, or essential for freight and evacuation. In complex intercity systems, road functionality can amplify losses, making this second-stage assessment central to operational planning and to comparing access benefits with wider corridor functions for emergency logistics and recovery (Kilanitis & Sextos, 2019).
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "The"
     - After: "Along the evaluated forward sequence, the"
  2. `replace`
     - Before: "sections"
     - After: "selections"
  3. `replace`
     - Before: "exhaust"
     - After: "supply"
  4. `replace`
     - Before: "positive"
     - After: "benefits"
  5. `replace`
     - Before: "benefit"
     - After: "shown"
  6. `replace`
     - Before: "available"
     - After: "in"
  7. `replace`
     - Before: "for"
     - After: "Figure"
  8. `replace`
     - Before: "the retained destinations"
     - After: "4"
  9. `replace`
     - Before: "and"
     - After: "with"
  10. `replace`
     - Before: "the"
     - After: "no"
  11. `replace`
     - Before: "plateau"
     - After: "additional gain"
  12. `replace`
     - Before: "larger"
     - After: "K=3"
  13. `replace`
     - Before: "portfolio"
     - After: "or"
  14. `replace`
     - Before: "sizes identifies redundancy in that access model"
     - After: "K=5"

### item-15

- Location: Approved item 15/24: KE03 / Discussion / Robustness, Transferability, and Operational Use
- Reason: 同步2套成员/4顺序，并纳入此次已验证的服务定义及分等级速度影响；保留闭路机制解释。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:13Z
- Author: Mike Li
- Markup SHA-256 before: `41091449d56cf34f595c7de9284b6fc8ae697f44beda39b876848364ffc2c6f4`
- Markup SHA-256 after: `e9287e278ab4534ac9e572d79e618ed00f6aea530780e3d026a0bc17343a4e18`
- Revision IDs: `899, 900, 901, 902, 903, 904, 905, 906, 907, 908`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232213314511.reviewer-4-comment-4.item-15.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
The robustness audit distinguishes active assumptions from nominal variation. Hazard threshold, facility availability, and settlement snapping change at least one aggregate access outcome, whereas the tested road-closure rule and topology threshold leave the three population-loss aggregates unchanged. The closure contrast changes component partitions and service travel times at 101–197 graph nodes while preserving the retained settlement-to-service estimands; every eligible settlement with a finite post-disruption path retains an equally short path avoiding the extra closures. Topology repair changes graph connectivity and adds one baseline-eligible settlement with zero event-induced loss, which explains why the loss aggregates remain unchanged. Population allocation and component weighting remain independent sources of rank movement, especially around the top-ten boundary. The 24 settlement-vector profiles, ten aggregate profiles, three top-ten orderings, and family-specific intervals provide more interpretable evidence than a pooled frequency over 192 nominal combinations and 10,000 random draws. This structure directs future sensitivity work toward assumptions that affect each decision outcome and identifies graph or coverage changes that totals alone conceal.
~~~~

- After:

~~~~text
The robustness audit distinguishes active assumptions from nominal variation. Hazard threshold, facility availability, and settlement snapping change at least one aggregate access outcome, whereas the tested road-closure rule and topology threshold leave the three population-loss aggregates unchanged. The closure contrast changes component partitions and service travel times at 101–197 graph nodes while preserving the retained settlement-to-service estimands; every eligible settlement with a finite post-disruption path retains an equally short path avoiding the extra closures. Topology repair changes graph connectivity and adds one baseline-eligible settlement with zero event-induced loss, which explains why the loss aggregates remain unchanged. Population allocation, component weighting, destination definition, and differential speeds provide additional sources of rank movement, especially around the top-ten boundary. The 24 settlement-vector profiles, ten aggregate profiles, two top-ten membership sets, four orderings, and family-specific intervals provide more interpretable evidence than a pooled frequency over 192 nominal combinations and 10,000 random draws. This structure directs future sensitivity work toward assumptions that affect each decision outcome and identifies graph or coverage changes that totals alone conceal.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: " and"
     - After: ","
  2. `insert`
     - Before: ""
     - After: ","
  3. `replace`
     - Before: "remain"
     - After: "destination"
  4. `replace`
     - Before: "independent"
     - After: "definition, and differential speeds provide additional"
  5. `replace`
     - Before: "three"
     - After: "two"
  6. `insert`
     - Before: ""
     - After: " membership sets, four"

### item-16

- Location: Approved item 16/24: KE03 / Discussion / Limitations and Future Validation / first paragraph
- Reason: 把审稿人要求的方向性、容量、拥堵、非正式道路及桥梁不完整性集中到既有Limitations，不在各段重复免责声明。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:13Z
- Author: Mike Li
- Markup SHA-256 before: `e9287e278ab4534ac9e572d79e618ed00f6aea530780e3d026a0bc17343a4e18`
- Markup SHA-256 after: `12d1abf26ccef7ca1a295700e4b34e08b89f406f31ddf94146718807daf37a9d`
- Revision IDs: `909`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232213833251.reviewer-4-comment-4.item-16.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Several limitations can alter the estimates in identifiable but not fully quantifiable directions. Incomplete optical evidence may miss or unevenly represent surface change, while the absent flow-path layer limits process-specific sensitivity beyond mapped, sensor, terrain, and channel agreement. Unobserved road and facility operation may overstate modeled access loss if alternatives remained usable or understate it if additional failures occurred. The same-local-unit rule leaves 29,133 of the unallocated people within 3 km of a settlement across a unit boundary. Changing the allocation threshold changes represented population without moving already assigned cells between settlements. Priorities therefore describe represented settlements with baseline access; unallocated and baseline-ineligible groups require a separate access-needs assessment. Coarse and uneven survey support weakens the vulnerability sensitivity and prevents local social conditions from entering the primary score. The road-restoration screen omits engineering feasibility, cost, repair time, capacity, and safety, which limits its use as a sequencing tool. None of these limitations can be resolved by additional numerical precision alone because each requires better observation, alternative evidence, or a broader decision model.
~~~~

- After:

~~~~text
Several limitations can alter the estimates in identifiable but not fully quantifiable directions. Incomplete optical evidence may miss or unevenly represent surface change, while the absent flow-path layer limits process-specific sensitivity beyond mapped, sensor, terrain, and channel agreement. The undirected graph omits one-way restrictions, congestion, and capacity limits, while unmapped informal routes and incompletely represented bridge damage can alter connectivity. Unobserved road and facility operation may overstate modeled access loss if alternatives remained usable or understate it if additional failures occurred. The same-local-unit rule leaves 29,133 of the unallocated people within 3 km of a settlement across a unit boundary. Changing the allocation threshold changes represented population without moving already assigned cells between settlements. Priorities therefore describe represented settlements with baseline access; unallocated and baseline-ineligible groups require a separate access-needs assessment. Coarse and uneven survey support weakens the vulnerability sensitivity and prevents local social conditions from entering the primary score. The road-restoration screen omits engineering feasibility, cost, repair time, capacity, and safety, which limits its use as a sequencing tool. None of these limitations can be resolved by additional numerical precision alone because each requires better observation, alternative evidence, or a broader decision model.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: ". The undirected graph omits one-way restrictions, congestion, and capacity limits, while unmapped informal routes and incompletely represented bridge damage can alter connectivity"

### item-17

- Location: Approved item 17/24: KE03 / Conclusion / existing restoration sentence
- Reason: 仅限定已有道路平台判断；全稿最终结论和贡献仍待其他分析gate后复审。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:14Z
- Author: Mike Li
- Markup SHA-256 before: `12d1abf26ccef7ca1a295700e4b34e08b89f406f31ddf94146718807daf37a9d`
- Markup SHA-256 after: `35bf6371055fb595c76c42fa1ec2993d44d85dfb4c377d543deb74901221795e`
- Revision IDs: `910`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232214371028.reviewer-4-comment-4.item-17.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
This study links multi-source hazard reconstruction with modeled population and network accessibility for Nepal's August 2026 rock-ice avalanche and flood corridor. The primary settlement ordering is driven by credible hazard evidence, represented population, and complete or severe access loss, while coarse social context is retained as an Appendix sensitivity. The 192 structural combinations produce 24 settlement-vector profiles and ten aggregate profiles; road closure and topology change graphs without changing the three population-loss aggregates. Separate allocation and weighting analyses show that uncertainty is concentrated near the lower end of the top-ten list. Joint rerouting distinguishes one road section that reconnects isolated population from another that reduces finite delay and reveals no additional modeled benefit beyond two sections. Together, these outputs create a traceable queue for field verification of settlements, services, and road sections. Current road operation, facility status, population presence, local needs, and engineering feasibility remain the observations most likely to change operational decisions.
~~~~

- After:

~~~~text
This study links multi-source hazard reconstruction with modeled population and network accessibility for Nepal's August 2026 rock-ice avalanche and flood corridor. The primary settlement ordering is driven by credible hazard evidence, represented population, and complete or severe access loss, while coarse social context is retained as an Appendix sensitivity. The 192 structural combinations produce 24 settlement-vector profiles and ten aggregate profiles; road closure and topology change graphs without changing the three population-loss aggregates. Separate allocation and weighting analyses show that uncertainty is concentrated near the lower end of the top-ten list. Joint rerouting distinguishes one road section that reconnects isolated population from another that reduces finite delay and reveals no additional modeled benefit beyond two sections along the evaluated forward sequence. Together, these outputs create a traceable queue for field verification of settlements, services, and road sections. Current road operation, facility status, population presence, local needs, and engineering feasibility remain the observations most likely to change operational decisions.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " along the evaluated forward sequence"

### item-18

- Location: Approved item 18/24: KE03 / Figures / Figure 2 explanatory note
- Reason: 图注与新设施点及访问图一致；现有panel和闭路说明保留。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:14Z
- Author: Mike Li
- Markup SHA-256 before: `35bf6371055fb595c76c42fa1ec2993d44d85dfb4c377d543deb74901221795e`
- Markup SHA-256 after: `9fca51a0a645996ea29c408813c15ef6f58c203b91b140608da1c1c428c55ee6`
- Revision IDs: `911, 912, 913, 914`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232214886855.reviewer-4-comment-4.item-18.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Note: Panel a maps full graph edges selected for modeled closure by both CEMS Destroyed grades and class-3 footprint intersection. Panel b shows baseline modeled access to retained health and emergency destinations. Panel c shows finite travel-time delays and settlements that become newly isolated under the primary disruption scenario.
~~~~

- After:

~~~~text
Note: Panel a maps full graph edges selected for modeled closure by both CEMS Destroyed grades and class-3 footprint intersection. Panel b shows baseline modeled access to 97 unique audited health and emergency destination nodes. Panel c shows finite travel-time delays and settlements that become newly isolated under the primary disruption scenario.
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "retained"
     - After: "97 unique audited"
  2. `replace`
     - Before: "destinations"
     - After: "destination nodes"

### item-19

- Location: Approved item 19/24: KE03 / Figures / Figure 4 explanatory note
- Reason: 图注的平台含义与正文一致，不作组合最优解释。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:15Z
- Author: Mike Li
- Markup SHA-256 before: `9fca51a0a645996ea29c408813c15ef6f58c203b91b140608da1c1c428c55ee6`
- Markup SHA-256 after: `0677dc6fd60568a307ad64b45086ea4683bf70d2de61bdcbd60f83ec9a353fd8`
- Revision IDs: `915`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232215389649.reviewer-4-comment-4.item-19.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Note: Panel a maps screened road sections and modeled beneficiary populations. Panel b separates benefits from reconnecting isolated populations and reducing finite travel delays for individual sections. Panel c compares jointly rerouted portfolios for K = 1, 2, 3, and 5, shows the benefit plateau after K = 2, and reports structural-scenario retention.
~~~~

- After:

~~~~text
Note: Panel a maps screened road sections and modeled beneficiary populations. Panel b separates benefits from reconnecting isolated populations and reducing finite travel delays for individual sections. Panel c compares jointly rerouted portfolios for K = 1, 2, 3, and 5, shows the forward-sequence benefit plateau after K = 2, and reports structural-scenario retention.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "forward-sequence "

### item-20-atom-001

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:34Z
- Author: Mike Li
- Markup SHA-256 before: `2d110ff77689616196f9890da8724c873390d639cf7a8b7d5d8589d8f983748f`
- Markup SHA-256 after: `e8af1579f899d0a8b08e4f767137742544256389ab9affd2d2b03640503aa8d4`
- Revision IDs: `2`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232234850852.reviewer-4-comment-4.item-20-atom-001.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
n order 
~~~~

- After:

~~~~text
n membership and order 
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: " membership and"

### item-20-atom-002

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:35Z
- Author: Mike Li
- Markup SHA-256 before: `e8af1579f899d0a8b08e4f767137742544256389ab9affd2d2b03640503aa8d4`
- Markup SHA-256 after: `0f18b75b7fc995b8d1003b316392ef94be8dd9297ff494bf55979f651d1b585d`
- Revision IDs: `2`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232235208439.reviewer-4-comment-4.item-20-atom-002.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ve 
~~~~

- After:

~~~~text
ve both 
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "both "

### item-20-atom-003

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:35Z
- Author: Mike Li
- Markup SHA-256 before: `0f18b75b7fc995b8d1003b316392ef94be8dd9297ff494bf55979f651d1b585d`
- Markup SHA-256 after: `3f18fb633fc0f358e96cb7a138c8126da84a88ec5924b678df0a683d1d730700`
- Revision IDs: `2`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232235581025.reviewer-4-comment-4.item-20-atom-003.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
factors l
~~~~

- After:

~~~~text
membership in 8 of 48 groups and order in 16. Road closure and topology l
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "factors"
     - After: "membership in 8 of 48 groups and order in 16. Road closure and topology"

### item-20-atom-004

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:35Z
- Author: Mike Li
- Markup SHA-256 before: `3f18fb633fc0f358e96cb7a138c8126da84a88ec5924b678df0a683d1d730700`
- Markup SHA-256 after: `90d82a2690de0575437cd69c75461fd8638828d759529baa55a057a4608e7496`
- Revision IDs: `2`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232235937834.reviewer-4-comment-4.item-20-atom-004.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
other m
~~~~

- After:

~~~~text
changes m
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "other"
     - After: "changes"

### item-20-atom-005

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:36Z
- Author: Mike Li
- Markup SHA-256 before: `90d82a2690de0575437cd69c75461fd8638828d759529baa55a057a4608e7496`
- Markup SHA-256 after: `ba34fad2a60bf2cb2209096764a8d411f53e087927574b3a824b7673bb3c8fe7`
- Revision IDs: `2`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232236306881.reviewer-4-comment-4.item-20-atom-005.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
; the
~~~~

- After:

~~~~text
; snapping
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "the"
     - After: "snapping"

### item-20-atom-006

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:36Z
- Author: Mike Li
- Markup SHA-256 before: `ba34fad2a60bf2cb2209096764a8d411f53e087927574b3a824b7673bb3c8fe7`
- Markup SHA-256 after: `9414f8ff38b83ac835351df03d3adc52fcb2bdf5e601ad42e2f7d12e8f30bf35`
- Revision IDs: `2`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232236675560.reviewer-4-comment-4.item-20-atom-006.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
48;
~~~~

- After:

~~~~text
96 groups and order in 32;
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "48"
     - After: "96 groups and order in 32"

### item-20-atom-007

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:37Z
- Author: Mike Li
- Markup SHA-256 before: `9414f8ff38b83ac835351df03d3adc52fcb2bdf5e601ad42e2f7d12e8f30bf35`
- Markup SHA-256 after: `ec78504d561407dee7173e8867adc9989d7fe037105a4458358e4f07ec4e9709`
- Revision IDs: `138, 139`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232237060403.reviewer-4-comment-4.item-20-atom-007.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
snapping i
~~~~

- After:

~~~~text
changes membership i
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "snapping"
     - After: "changes membership"

### item-20-atom-008

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:37Z
- Author: Mike Li
- Markup SHA-256 before: `ec78504d561407dee7173e8867adc9989d7fe037105a4458358e4f07ec4e9709`
- Markup SHA-256 after: `1db7f200eb8235821eae2adb14e3107fc44c6cddda6f0836b6fa690ee7d02bae`
- Revision IDs: `140, 141`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232237446546.reviewer-4-comment-4.item-20-atom-008.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
settlement c
~~~~

- After:

~~~~text
availability c
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "settlement"
     - After: "availability"

### item-20-atom-009

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:37Z
- Author: Mike Li
- Markup SHA-256 before: `1db7f200eb8235821eae2adb14e3107fc44c6cddda6f0836b6fa690ee7d02bae`
- Markup SHA-256 after: `e75c46b4eb1ab08c0d156724183fd1f6aea0ad83a9014b9e6e1b5d8af115395a`
- Revision IDs: `142, 143`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232237826003.reviewer-4-comment-4.item-20-atom-009.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
and a
~~~~

- After:

~~~~text
facility a
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "and"
     - After: "facility"

### item-20-atom-010

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:38Z
- Author: Mike Li
- Markup SHA-256 before: `e75c46b4eb1ab08c0d156724183fd1f6aea0ad83a9014b9e6e1b5d8af115395a`
- Markup SHA-256 after: `06ac97a9c3f548229691c8c59ecffbdb5a59d1bfd47d0f6a87f14f108d685187`
- Revision IDs: `144`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232238195686.reviewer-4-comment-4.item-20-atom-010.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ps f
~~~~

- After:

~~~~text
ps; f
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: ";"

### item-20-atom-011

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:38Z
- Author: Mike Li
- Markup SHA-256 before: `06ac97a9c3f548229691c8c59ecffbdb5a59d1bfd47d0f6a87f14f108d685187`
- Markup SHA-256 after: `dbe18a38206f70b97c8f588fb1656e70f323d780640665e2ba75a0c898561d60`
- Revision IDs: `3`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232238556708.reviewer-4-comment-4.item-20-atom-011.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
2 of
~~~~

- After:

~~~~text
2 
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "of"
     - After: ""

### item-20-atom-012

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:38Z
- Author: Mike Li
- Markup SHA-256 before: `dbe18a38206f70b97c8f588fb1656e70f323d780640665e2ba75a0c898561d60`
- Markup SHA-256 after: `f93ae23d083c60b74802e67b1d751bcd9bfcfe3fb29b450731283920603de3b4`
- Revision IDs: `145, 146`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232238935691.reviewer-4-comment-4.item-20-atom-012.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
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
all
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "32 "
     - After: "all"

### item-20-atom-013

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:39Z
- Author: Mike Li
- Markup SHA-256 before: `f93ae23d083c60b74802e67b1d751bcd9bfcfe3fb29b450731283920603de3b4`
- Markup SHA-256 after: `28f372669e7f59c5776c0f2e143362802728545f5c5a778a2173aeb926f0bd04`
- Revision IDs: `147`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232239325010.reviewer-4-comment-4.item-20-atom-013.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
s or
~~~~

- After:

~~~~text
s membership and or
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "membership and "

### item-20-atom-014

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:39Z
- Author: Mike Li
- Markup SHA-256 before: `28f372669e7f59c5776c0f2e143362802728545f5c5a778a2173aeb926f0bd04`
- Markup SHA-256 after: `4633b7ba25a0cd41faf067943b94ecdbae3febf8a3975a896258c899cbdaed0d`
- Revision IDs: `148, 149`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232239728221.reviewer-4-comment-4.item-20-atom-014.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 hazard
~~~~

- After:

~~~~text
 two top-ten membership sets with nine common members and four orderings. Hazard
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "hazard"
     - After: "two top-ten membership sets with nine common members and four orderings. Hazard"

### item-20-atom-015

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:40Z
- Author: Mike Li
- Markup SHA-256 before: `4633b7ba25a0cd41faf067943b94ecdbae3febf8a3975a896258c899cbdaed0d`
- Markup SHA-256 after: `d458e9b7838ace3c5cefdbc779d1140c82af8f305775fa91363159f3d36ae635`
- Revision IDs: `150, 151`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232240123463.reviewer-4-comment-4.item-20-atom-015.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
, while
~~~~

- After:

~~~~text
, yield
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "while"
     - After: "yield"

### item-20-atom-016

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:40Z
- Author: Mike Li
- Markup SHA-256 before: `d458e9b7838ace3c5cefdbc779d1140c82af8f305775fa91363159f3d36ae635`
- Markup SHA-256 after: `b18165f2417e24c9143fa9566bb303a612cacc2c9e3950f900a9f51db2ace2b6`
- Revision IDs: `152`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232240520087.reviewer-4-comment-4.item-20-atom-016.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
ns,
~~~~

- After:

~~~~text
ns
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: ","
     - After: ""

### item-20-atom-017

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:40Z
- Author: Mike Li
- Markup SHA-256 before: `b18165f2417e24c9143fa9566bb303a612cacc2c9e3950f900a9f51db2ace2b6`
- Markup SHA-256 after: `297b19af151ae1624803b05cb05f4a8b8ea61b26bec43ca067313e8c49c60ce3`
- Revision IDs: `153`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232240909430.reviewer-4-comment-4.item-20-atom-017.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
 all 1
~~~~

- After:

~~~~text
 1
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " all"
     - After: ""

### item-20-atom-018

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:41Z
- Author: Mike Li
- Markup SHA-256 before: `297b19af151ae1624803b05cb05f4a8b8ea61b26bec43ca067313e8c49c60ce3`
- Markup SHA-256 after: `c31ff70d4ca04cb21be4d34f1fb5c4f494d3ba3c0082ae3b22abaa5f1b38507b`
- Revision IDs: `10`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232241294607.reviewer-4-comment-4.item-20-atom-018.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
across
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "across"
     - After: ""

### item-20-atom-019

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:41Z
- Author: Mike Li
- Markup SHA-256 before: `c31ff70d4ca04cb21be4d34f1fb5c4f494d3ba3c0082ae3b22abaa5f1b38507b`
- Markup SHA-256 after: `eca2bab4cc75bd17e0f411b86ec3a1c2cabbfcc99ca5b1b9c65ec67b8404a34e`
- Revision IDs: `154`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232241693380.reviewer-4-comment-4.item-20-atom-019.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
sts 
~~~~

- After:

~~~~text
sts
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-20-atom-020

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:42Z
- Author: Mike Li
- Markup SHA-256 before: `eca2bab4cc75bd17e0f411b86ec3a1c2cabbfcc99ca5b1b9c65ec67b8404a34e`
- Markup SHA-256 after: `fc8c76b0f98d68e8452bd585702759c1ae93cfa0182b5748e2651d81d849de74`
- Revision IDs: `12`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232242079214.reviewer-4-comment-4.item-20-atom-020.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
persists
~~~~

- After:

~~~~text

~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "persists"
     - After: ""

### item-20-atom-021

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:42Z
- Author: Mike Li
- Markup SHA-256 before: `fc8c76b0f98d68e8452bd585702759c1ae93cfa0182b5748e2651d81d849de74`
- Markup SHA-256 after: `89b9d245c7ccbdd1dcfd33976836a04d8558bb2108377fdb101387ab234acdf2`
- Revision IDs: `155`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232242472077.reviewer-4-comment-4.item-20-atom-021.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Top-ten membership 
~~~~

- After:

~~~~text
Top-ten membership
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-20-atom-022

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:42Z
- Author: Mike Li
- Markup SHA-256 before: `89b9d245c7ccbdd1dcfd33976836a04d8558bb2108377fdb101387ab234acdf2`
- Markup SHA-256 after: `d6c5b689a5365709a42a9b8d2e47410b7dc1aa05fe94133711584ea2265f4272`
- Revision IDs: `14`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232242856520.reviewer-4-comment-4.item-20-atom-022.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
membership 1
~~~~

- After:

~~~~text
 1
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: "membership"
     - After: ""

### item-20-atom-023

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:22:43Z
- Author: Mike Li
- Markup SHA-256 before: `d6c5b689a5365709a42a9b8d2e47410b7dc1aa05fe94133711584ea2265f4272`
- Markup SHA-256 after: `6d8bfcb065f7ae971efd19efd7a7e100e66bfdf27e758c069a101c24b49d21b8`
- Revision IDs: `156`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232243237160.reviewer-4-comment-4.item-20-atom-023.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Top-ten 
~~~~

- After:

~~~~text
Top-ten
~~~~

- Minimal tracked fragments:
  1. `delete`
     - Before: " "
     - After: ""

### item-20-atom-024

- Location: Approved item 20/24: Appendix / Appendix A / Accessibility and Priority Robustness / structural audit
- Reason: 同步A1末两列和完整192新主结果，保留仍成立的节点、连接边、43.31分钟及见证机制。
- Kila decisions: KILA-D-20261023-014
- Mode: `reedit`
- Revises prior parts: reviewer-4/comment-7#part-10
- Timestamp: 2026-10-23T14:22:43Z
- Author: Mike Li
- Markup SHA-256 before: `6d8bfcb065f7ae971efd19efd7a7e100e66bfdf27e758c069a101c24b49d21b8`
- Markup SHA-256 after: `a072bb5939f5c31cc1fc7d1287547a116f5f779a99abc1603b841f8c78473fb8`
- Revision IDs: `16`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232243598318.reviewer-4-comment-4.item-20-atom-024.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Top-ten
~~~~

- After:

~~~~text
The
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Top-ten"
     - After: "The"

### item-21

- Location: Approved item 21/24: Appendix / Appendix A / Accessibility and Priority Robustness / Figure A2 interpretation
- Reason: 避免把整数显示的100%误读为所有权重规格均保持，和新FigureA2/主文一致。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:11Z
- Author: Mike Li
- Markup SHA-256 before: `a072bb5939f5c31cc1fc7d1287547a116f5f779a99abc1603b841f8c78473fb8`
- Markup SHA-256 after: `fe928465c349fde5613c3b0b6d928a0ab3ac901678adeeced59979f8849826d4`
- Revision IDs: `157, 158, 159, 160, 161`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232311394062.reviewer-4-comment-4.item-21.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Appendix Figure A2 compares primary score, allocation top-ten persistence, and weight-rule top-ten persistence for the leading 20 settlements. Its second panel shows structural and allocation min–max ranks, weight-rule P05–P95 intervals, and the primary rank. The first four settlements remain fixed under structural assumptions and remain in the top ten under all allocation and weighting specifications. Intervals widen below the leading group, especially for the random-weight family. The display preserves the source of rank movement without a pooled stability statistic. The geometric score below supplies the multiplicative robustness specification used alongside the additive alternatives.
~~~~

- After:

~~~~text
Appendix Figure A2 compares primary score, allocation top-ten persistence, and weight-rule top-ten persistence for the leading 20 settlements. Its second panel shows structural and allocation min–max ranks, weight-rule P05–P95 intervals, and the primary rank. The first four settlements remain fixed under structural assumptions and remain in the top ten under all allocation thresholds; weight-rule persistence is 100% for the first three and 99.85% for Betrawati. Intervals widen below the leading group, especially for the random-weight family. The display preserves the source of rank movement without a pooled stability statistic. The geometric score below supplies the multiplicative robustness specification used alongside the additive alternatives.
~~~~

- Minimal tracked fragments:
  1. `insert`
     - Before: ""
     - After: "thresholds; weight-rule persistence is 100% for the first three "
  2. `replace`
     - Before: "weighting"
     - After: "99.85%"
  3. `replace`
     - Before: "specifications"
     - After: "for Betrawati"

### item-22-cell-01

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:11Z
- Author: Mike Li
- Markup SHA-256 before: `0677dc6fd60568a307ad64b45086ea4683bf70d2de61bdcbd60f83ec9a353fd8`
- Markup SHA-256 after: `23062c2c117aac543dcaec0334150f602aa81d20cf0ce677e0c1b2040cbc09dd`
- Revision IDs: `916, 917`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232311881992.reviewer-4-comment-4.item-22-cell-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.948
~~~~

- After:

~~~~text
0.943
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "948"
     - After: "943"

### item-22-cell-02

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:12Z
- Author: Mike Li
- Markup SHA-256 before: `23062c2c117aac543dcaec0334150f602aa81d20cf0ce677e0c1b2040cbc09dd`
- Markup SHA-256 after: `58684c82bfeca0a8687ddbd1a081ce227541397bf80fccd8efe2838d4fb86117`
- Revision IDs: `918, 919`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232312310519.reviewer-4-comment-4.item-22-cell-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.940
~~~~

- After:

~~~~text
0.936
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "940"
     - After: "936"

### item-22-cell-03

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:12Z
- Author: Mike Li
- Markup SHA-256 before: `58684c82bfeca0a8687ddbd1a081ce227541397bf80fccd8efe2838d4fb86117`
- Markup SHA-256 after: `f8e303f06ab244c3490a69fc7921befdbb3109ac80ff5fc4cb5c29c1fbce605e`
- Revision IDs: `920, 921`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232312737347.reviewer-4-comment-4.item-22-cell-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.936
~~~~

- After:

~~~~text
0.932
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "936"
     - After: "932"

### item-22-cell-04

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:13Z
- Author: Mike Li
- Markup SHA-256 before: `f8e303f06ab244c3490a69fc7921befdbb3109ac80ff5fc4cb5c29c1fbce605e`
- Markup SHA-256 after: `83ef47db7354e3cff7c76bdc9c54591f63ef75d5491e977585e1cf366df7bbbd`
- Revision IDs: `922, 923`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232313175222.reviewer-4-comment-4.item-22-cell-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.920
~~~~

- After:

~~~~text
0.917
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "920"
     - After: "917"

### item-22-cell-05

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:13Z
- Author: Mike Li
- Markup SHA-256 before: `83ef47db7354e3cff7c76bdc9c54591f63ef75d5491e977585e1cf366df7bbbd`
- Markup SHA-256 after: `c4912bdf711a1892871e454f9f710a3b84b8344ac3cb4d6efd2322332ac92db2`
- Revision IDs: `924, 925`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232313609833.reviewer-4-comment-4.item-22-cell-05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.904
~~~~

- After:

~~~~text
0.902
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "904"
     - After: "902"

### item-22-cell-06

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:13Z
- Author: Mike Li
- Markup SHA-256 before: `c4912bdf711a1892871e454f9f710a3b84b8344ac3cb4d6efd2322332ac92db2`
- Markup SHA-256 after: `06576bd22d31b91aef74eb8c5d822303fb8b79feedc6829dfcc319e9e68d14bf`
- Revision IDs: `926, 927`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232314058103.reviewer-4-comment-4.item-22-cell-06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
99%
~~~~

- After:

~~~~text
98%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "99"
     - After: "98"

### item-22-cell-07

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:14Z
- Author: Mike Li
- Markup SHA-256 before: `06576bd22d31b91aef74eb8c5d822303fb8b79feedc6829dfcc319e9e68d14bf`
- Markup SHA-256 after: `a7c8d981cd6da78c5cd0fcd7d36471143f4ad2871136f273f4b9504cf5148c0b`
- Revision IDs: `928, 929`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232314488369.reviewer-4-comment-4.item-22-cell-07.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.863
~~~~

- After:

~~~~text
0.860
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "863"
     - After: "860"

### item-22-cell-08

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:14Z
- Author: Mike Li
- Markup SHA-256 before: `a7c8d981cd6da78c5cd0fcd7d36471143f4ad2871136f273f4b9504cf5148c0b`
- Markup SHA-256 after: `03a6368fb04865060b43bdd0a432dbb141d584abd4655e58b66cd664ba2f681f`
- Revision IDs: `930, 931`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232314941666.reviewer-4-comment-4.item-22-cell-08.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
92%
~~~~

- After:

~~~~text
87%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "92"
     - After: "87"

### item-22-cell-09

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:15Z
- Author: Mike Li
- Markup SHA-256 before: `03a6368fb04865060b43bdd0a432dbb141d584abd4655e58b66cd664ba2f681f`
- Markup SHA-256 after: `3349af27241e4980bb410b08dcb3e1a5385a98c41e70e93d4561ed577e2964e6`
- Revision IDs: `932, 933`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232315394485.reviewer-4-comment-4.item-22-cell-09.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.803
~~~~

- After:

~~~~text
0.799
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "803"
     - After: "799"

### item-22-cell-10

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:15Z
- Author: Mike Li
- Markup SHA-256 before: `3349af27241e4980bb410b08dcb3e1a5385a98c41e70e93d4561ed577e2964e6`
- Markup SHA-256 after: `3e815ea6ad6cb434aee04fa67766dffee3c3d2d767744e9e4720e3388d5fe61d`
- Revision IDs: `934, 935`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232315823695.reviewer-4-comment-4.item-22-cell-10.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
7–9
~~~~

- After:

~~~~text
7–7
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "9"
     - After: "7"

### item-22-cell-11

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:16Z
- Author: Mike Li
- Markup SHA-256 before: `3e815ea6ad6cb434aee04fa67766dffee3c3d2d767744e9e4720e3388d5fe61d`
- Markup SHA-256 after: `8c3bad9c6b724e02152d00f39e4fa5d760fabed1bb18775f3336544e1114f99f`
- Revision IDs: `936, 937`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232316276357.reviewer-4-comment-4.item-22-cell-11.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
67%
~~~~

- After:

~~~~text
63%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "67"
     - After: "63"

### item-22-cell-12

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:16Z
- Author: Mike Li
- Markup SHA-256 before: `8c3bad9c6b724e02152d00f39e4fa5d760fabed1bb18775f3336544e1114f99f`
- Markup SHA-256 after: `d4aff7633a3414b23fb3da5a71ab65f2630d7311abef05a34adf7e6c3a949742`
- Revision IDs: `938, 939, 940, 941`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232316707487.reviewer-4-comment-4.item-22-cell-12.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Unnamed settlement (OSM 3478460439)
Tarakeshwor, Nuwakot
~~~~

- After:

~~~~text
Unnamed settlement (OSM 3478285246)
Bidur, Nuwakot
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "3478460439"
     - After: "3478285246"
  2. `replace`
     - Before: "Tarakeshwor"
     - After: "Bidur"

### item-22-cell-13

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:17Z
- Author: Mike Li
- Markup SHA-256 before: `d4aff7633a3414b23fb3da5a71ab65f2630d7311abef05a34adf7e6c3a949742`
- Markup SHA-256 after: `e70b5df39202b1c939eaba6d36cb1e69a411de2919ccb61990fca8f2f6f6d5de`
- Revision IDs: `942, 943`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232317162545.reviewer-4-comment-4.item-22-cell-13.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
1,596
~~~~

- After:

~~~~text
872
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "1,596"
     - After: "872"

### item-22-cell-14

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:17Z
- Author: Mike Li
- Markup SHA-256 before: `e70b5df39202b1c939eaba6d36cb1e69a411de2919ccb61990fca8f2f6f6d5de`
- Markup SHA-256 after: `dfbd9e750b36875587b826ee6e32a569f99a419bf277688b2c2bad9c5a853d53`
- Revision IDs: `944, 945`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232317587077.reviewer-4-comment-4.item-22-cell-14.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.799
~~~~

- After:

~~~~text
0.787
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "799"
     - After: "787"

### item-22-cell-15

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:17Z
- Author: Mike Li
- Markup SHA-256 before: `dfbd9e750b36875587b826ee6e32a569f99a419bf277688b2c2bad9c5a853d53`
- Markup SHA-256 after: `9ed3f08f714e003db147b195707d40a761874702e5f691f183ba1a620844281e`
- Revision IDs: `946, 947`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232318023412.reviewer-4-comment-4.item-22-cell-15.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
53%
~~~~

- After:

~~~~text
47%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "53"
     - After: "47"

### item-22-cell-16

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:18Z
- Author: Mike Li
- Markup SHA-256 before: `9ed3f08f714e003db147b195707d40a761874702e5f691f183ba1a620844281e`
- Markup SHA-256 after: `ffac95df27a9269c73f5ccf5041c572239c533c1c4244dc6fe37c7e752bf1c7d`
- Revision IDs: `948, 949, 950, 951`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232318478936.reviewer-4-comment-4.item-22-cell-16.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Gerkhu
Bidur, Nuwakot
~~~~

- After:

~~~~text
Unnamed settlement (OSM 3478460439)
Tarakeshwor, Nuwakot
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Gerkhu"
     - After: "Unnamed settlement (OSM 3478460439)"
  2. `replace`
     - Before: "Bidur"
     - After: "Tarakeshwor"

### item-22-cell-17

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:18Z
- Author: Mike Li
- Markup SHA-256 before: `ffac95df27a9269c73f5ccf5041c572239c533c1c4244dc6fe37c7e752bf1c7d`
- Markup SHA-256 after: `3e053c762878a6475e1aaa52338b8cc5fe3f8110ceb42bc16bbd88b86b37ac79`
- Revision IDs: `952, 953, 954, 955`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232318905717.reviewer-4-comment-4.item-22-cell-17.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
2,282
~~~~

- After:

~~~~text
1,596
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "2"
     - After: "1"
  2. `replace`
     - Before: "282"
     - After: "596"

### item-22-cell-18

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:19Z
- Author: Mike Li
- Markup SHA-256 before: `3e053c762878a6475e1aaa52338b8cc5fe3f8110ceb42bc16bbd88b86b37ac79`
- Markup SHA-256 after: `e1a49b42d70579e382d168cb0bf80d5be67f0db15a3895ce27859fcfaa879366`
- Revision IDs: `956, 957`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232319350744.reviewer-4-comment-4.item-22-cell-18.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.799
~~~~

- After:

~~~~text
0.769
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "799"
     - After: "769"

### item-22-cell-19

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:19Z
- Author: Mike Li
- Markup SHA-256 before: `e1a49b42d70579e382d168cb0bf80d5be67f0db15a3895ce27859fcfaa879366`
- Markup SHA-256 after: `7710fed477abc9bf2f81918ecd57d8fbd8f81cedc282eb276ee4c116a8828223`
- Revision IDs: `958, 959`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232319801365.reviewer-4-comment-4.item-22-cell-19.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
7–9
~~~~

- After:

~~~~text
8–9
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "7"
     - After: "8"

### item-22-cell-20

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:20Z
- Author: Mike Li
- Markup SHA-256 before: `7710fed477abc9bf2f81918ecd57d8fbd8f81cedc282eb276ee4c116a8828223`
- Markup SHA-256 after: `59458f0a6a1d8f8bdbf9e881f138f1f7fca60f60114ae5924f79faa56d880088`
- Revision IDs: `960, 961`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232320235269.reviewer-4-comment-4.item-22-cell-20.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
75%
~~~~

- After:

~~~~text
100%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "75"
     - After: "100"

### item-22-cell-21

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:20Z
- Author: Mike Li
- Markup SHA-256 before: `59458f0a6a1d8f8bdbf9e881f138f1f7fca60f60114ae5924f79faa56d880088`
- Markup SHA-256 after: `bce7eda45dc23be61dd01027f13794b0996a87b96408258aefe0d1db5012da70`
- Revision IDs: `962, 963`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232320656144.reviewer-4-comment-4.item-22-cell-21.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
53%
~~~~

- After:

~~~~text
37%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "53"
     - After: "37"

### item-22-cell-22

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:20Z
- Author: Mike Li
- Markup SHA-256 before: `bce7eda45dc23be61dd01027f13794b0996a87b96408258aefe0d1db5012da70`
- Markup SHA-256 after: `0207da325a31a97518ea85d038d397e578ee9e06abc65c27a1654d02171f9d18`
- Revision IDs: `964, 965`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232321087216.reviewer-4-comment-4.item-22-cell-22.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
Unnamed settlement (OSM 3478285246)
Bidur, Nuwakot
~~~~

- After:

~~~~text
Gerkhu
Bidur, Nuwakot
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "Unnamed settlement (OSM 3478285246)"
     - After: "Gerkhu"

### item-22-cell-23

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:21Z
- Author: Mike Li
- Markup SHA-256 before: `0207da325a31a97518ea85d038d397e578ee9e06abc65c27a1654d02171f9d18`
- Markup SHA-256 after: `69e1e0c692fbaf7b1371e9b9fd7bfd9ff6b487f695779bab8ff8cfc97f42057f`
- Revision IDs: `966, 967`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232321535291.reviewer-4-comment-4.item-22-cell-23.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
872
~~~~

- After:

~~~~text
2,282
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "872"
     - After: "2,282"

### item-22-cell-24

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:21Z
- Author: Mike Li
- Markup SHA-256 before: `69e1e0c692fbaf7b1371e9b9fd7bfd9ff6b487f695779bab8ff8cfc97f42057f`
- Markup SHA-256 after: `19c20c00a53d4a9238e3cce9780051b87d4bb4e40c3a62f3247023439b0f4ed9`
- Revision IDs: `968, 969`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232321986975.reviewer-4-comment-4.item-22-cell-24.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
0.773
~~~~

- After:

~~~~text
0.739
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "773"
     - After: "739"

### item-22-cell-25

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:22Z
- Author: Mike Li
- Markup SHA-256 before: `19c20c00a53d4a9238e3cce9780051b87d4bb4e40c3a62f3247023439b0f4ed9`
- Markup SHA-256 after: `e56a77d28fc81331826968af7830e6c69c039cdbf2efd6079b54f1ce84b24a09`
- Revision IDs: `970, 971`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232322420726.reviewer-4-comment-4.item-22-cell-25.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
10–10
~~~~

- After:

~~~~text
10–11
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "10"
     - After: "11"

### item-22-cell-26

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:22Z
- Author: Mike Li
- Markup SHA-256 before: `e56a77d28fc81331826968af7830e6c69c039cdbf2efd6079b54f1ce84b24a09`
- Markup SHA-256 after: `b8587e67be35cc14bf8022d82bab0c0efeee442581a9d472ad6f57c161c4e20e`
- Revision IDs: `972, 973`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232322853359.reviewer-4-comment-4.item-22-cell-26.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
75%
~~~~

- After:

~~~~text
25%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "75"
     - After: "25"

### item-22-cell-27

- Location: Approved item 22/24: KE03 / Table 2. Top ten priority settlements
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:23:23Z
- Author: Mike Li
- Markup SHA-256 before: `b8587e67be35cc14bf8022d82bab0c0efeee442581a9d472ad6f57c161c4e20e`
- Markup SHA-256 after: `6e556f2f1da3776c6b2874e588cd759e04e41592ff9af1c32202d75eb1c4484d`
- Revision IDs: `974, 975`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232323314741.reviewer-4-comment-4.item-22-cell-27.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `66def47a11e4925a07e8f23c5664f35669d5b156ee9513a0a47d1caa573bc348`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
36%
~~~~

- After:

~~~~text
31%
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "36"
     - After: "31"

### item-23-cell-01

- Location: Approved item 23/24: KE03 / Table 3. Road-repair screening and portfolio scenarios
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:16Z
- Author: Mike Li
- Markup SHA-256 before: `6e556f2f1da3776c6b2874e588cd759e04e41592ff9af1c32202d75eb1c4484d`
- Markup SHA-256 after: `937e56cdc23b53b88770c52e8ae9fa6f2f17a3eb7d2b3b73ade9088f907879b3`
- Revision IDs: `976, 977, 978, 979`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232416248006.reviewer-4-comment-4.item-23-cell-01.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
121,986
~~~~

- After:

~~~~text
55,087
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"

### item-23-cell-02

- Location: Approved item 23/24: KE03 / Table 3. Road-repair screening and portfolio scenarios
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:16Z
- Author: Mike Li
- Markup SHA-256 before: `937e56cdc23b53b88770c52e8ae9fa6f2f17a3eb7d2b3b73ade9088f907879b3`
- Markup SHA-256 after: `d6ad8b094b3e776f28140241d3e04fda9ced4bfe4ee999ba8da0b1f771285b11`
- Revision IDs: `980, 981, 982, 983`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232416669277.reviewer-4-comment-4.item-23-cell-02.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
121,986
~~~~

- After:

~~~~text
55,087
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"

### item-23-cell-03

- Location: Approved item 23/24: KE03 / Table 3. Road-repair screening and portfolio scenarios
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:16Z
- Author: Mike Li
- Markup SHA-256 before: `d6ad8b094b3e776f28140241d3e04fda9ced4bfe4ee999ba8da0b1f771285b11`
- Markup SHA-256 after: `26599462dd94cb99d61f910dd8c5f5c039d0642dda56e1c77695ff0dda784068`
- Revision IDs: `984, 985, 986, 987`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232417098225.reviewer-4-comment-4.item-23-cell-03.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
121,986
~~~~

- After:

~~~~text
55,087
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"

### item-23-cell-04

- Location: Approved item 23/24: KE03 / Table 3. Road-repair screening and portfolio scenarios
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:17Z
- Author: Mike Li
- Markup SHA-256 before: `26599462dd94cb99d61f910dd8c5f5c039d0642dda56e1c77695ff0dda784068`
- Markup SHA-256 after: `938745558029d64f53d70d276e20cb8a6adbb9abb9bf7a9b694940164d331ca0`
- Revision IDs: `988, 989, 990, 991`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232417520724.reviewer-4-comment-4.item-23-cell-04.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
121,986
~~~~

- After:

~~~~text
55,087
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"

### item-23-cell-05

- Location: Approved item 23/24: KE03 / Table 3. Road-repair screening and portfolio scenarios
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:17Z
- Author: Mike Li
- Markup SHA-256 before: `938745558029d64f53d70d276e20cb8a6adbb9abb9bf7a9b694940164d331ca0`
- Markup SHA-256 after: `c47f488bad058c33e489bef4c98eda82e48d2a4eca5d7763336b88f0e2e62d67`
- Revision IDs: `992, 993, 994, 995`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232417946721.reviewer-4-comment-4.item-23-cell-05.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
121,986
~~~~

- After:

~~~~text
55,087
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"

### item-23-cell-06

- Location: Approved item 23/24: KE03 / Table 3. Road-repair screening and portfolio scenarios
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:18Z
- Author: Mike Li
- Markup SHA-256 before: `c47f488bad058c33e489bef4c98eda82e48d2a4eca5d7763336b88f0e2e62d67`
- Markup SHA-256 after: `74869de1d36548947151ed0e090f35e14e937ccb4818db6fb882edfe369f1b1a`
- Revision IDs: `996, 997, 998, 999`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/KE03.rev.markup.20261023T232418385265.reviewer-4-comment-4.item-23-cell-06.docx`
- Paragraph properties preserved: `true`
- Run style source SHA-256: `c21d00426c037a67b0fba1fabff610e453e3a2a5424274c5287e40c65ce00d46`
- Formula verification: not applicable
- Endnote hyperlinks preserved: `true`
- Endnote hyperlink count: `0`
- Endnote hyperlink XML SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Endnote relationships SHA-256: `absent`
- Before:

~~~~text
121,986
~~~~

- After:

~~~~text
55,087
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "121"
     - After: "55"
  2. `replace`
     - Before: "986"
     - After: "087"

### item-24-cell-01

- Location: Approved item 24/24: Appendix / Appendix Table A1. Structural scenario factor activity
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:18Z
- Author: Mike Li
- Markup SHA-256 before: `fe928465c349fde5613c3b0b6d928a0ab3ac901678adeeced59979f8849826d4`
- Markup SHA-256 after: `308f6608f76130bf98a597925fc8ccf09a08a59eb7168f0526b70e386c2a7501`
- Revision IDs: `162, 163`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232418710182.reviewer-4-comment-4.item-24-cell-01.docx`
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
64
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "64"

### item-24-cell-02

- Location: Approved item 24/24: Appendix / Appendix Table A1. Structural scenario factor activity
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:18Z
- Author: Mike Li
- Markup SHA-256 before: `308f6608f76130bf98a597925fc8ccf09a08a59eb7168f0526b70e386c2a7501`
- Markup SHA-256 after: `062044521fb37b8790aab127685896117db14f97883e8f526646e857ec51d030`
- Revision IDs: `164, 165`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232418952302.reviewer-4-comment-4.item-24-cell-02.docx`
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
64
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "32"
     - After: "64"

### item-24-cell-03

- Location: Approved item 24/24: Appendix / Appendix Table A1. Structural scenario factor activity
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:19Z
- Author: Mike Li
- Markup SHA-256 before: `062044521fb37b8790aab127685896117db14f97883e8f526646e857ec51d030`
- Markup SHA-256 after: `c9cfe712bbc8cdbff521aefce377ea8aa16049ed6422fbbcdc2771900d9ba66c`
- Revision IDs: `166, 167`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232419211087.reviewer-4-comment-4.item-24-cell-03.docx`
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
16
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "16"

### item-24-cell-04

- Location: Approved item 24/24: Appendix / Appendix Table A1. Structural scenario factor activity
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:19Z
- Author: Mike Li
- Markup SHA-256 before: `c9cfe712bbc8cdbff521aefce377ea8aa16049ed6422fbbcdc2771900d9ba66c`
- Markup SHA-256 after: `1b4218a324a210f70b774e7949ad44a21727cb09c1843c0c9ec5f06f463976b3`
- Revision IDs: `168, 169`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232419459029.reviewer-4-comment-4.item-24-cell-04.docx`
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
32
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "32"

### item-24-cell-05

- Location: Approved item 24/24: Appendix / Appendix Table A1. Structural scenario factor activity
- Reason: 以严格原生表格单元格定位逐格true tracked更新，不替换表对象或改变列宽/换行。
- Kila decisions: KILA-D-20261023-014
- Mode: `replace`
- Revises prior parts: none
- Timestamp: 2026-10-23T14:24:19Z
- Author: Mike Li
- Markup SHA-256 before: `1b4218a324a210f70b774e7949ad44a21727cb09c1843c0c9ec5f06f463976b3`
- Markup SHA-256 after: `9322080f213eaf82f3f910f0c47eaca190779d283373323e06935b87cce5e351`
- Revision IDs: `170, 171`
- Backup: `/Volumes/Extension/Research/KE03/Rev/revision/.kila-backups/Appendix.rev.markup.20261023T232419704875.reviewer-4-comment-4.item-24-cell-05.docx`
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
8
~~~~

- Minimal tracked fragments:
  1. `replace`
     - Before: "0"
     - After: "8"

