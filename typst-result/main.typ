#import "@preview/modern-g7-32:0.2.0": gost, abstract

#show: gost.with(
  ministry: "МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
  organization: (
    full: "ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ ВЫСШЕГО ОБРАЗОВАНИЯ «МОСКОВСКИЙ АВИАЦИОННЫЙ ИНСТИТУТ (НАЦИОНАЛЬНЫЙ ИССЛЕДОВАТЕЛЬСКИЙ УНИВЕРСИТЕТ)»",
    short: "МАИ",
  ),
  subject: "Оптимизация холодного старта и масштабирования моделей машинного обучения в бессерверном инференсе для обеспечения надёжности и высокой доступности",
  city: "Москва",
  year: 2025,
  performers: ((name: "TODO: ФИО студента", position: "студент группы TODO"),),
  manager: (name: "TODO: ФИО руководителя", position: "TODO: должность", title: "TODO: учёная степень"),
)

#include "contents/0-abstract.typ"

#outline(title: [Содержание])

#include "contents/terms.typ"
#include "contents/abbreviations.typ"
#include "contents/1-introduction.typ"
#include "contents/1_1-cold-start.typ"
#include "contents/2_1-existing-solutions.typ"
#include "contents/3_1-nfs-stage.typ"
#include "contents/4_1-p2p-fuse.typ"
#include "contents/5_1-evaluation.typ"
#include "contents/6-conclusion.typ"

#bibliography("main.bib", style: "ieee", title: [Список использованных источников])
