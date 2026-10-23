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

