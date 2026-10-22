# ▲ MindChess · Tablero de Crecimiento

Ajedrez clásico con una capa reflexiva: asigna fortalezas a tus piezas, supera las debilidades del rival y gana XP.

## Contenido
| Archivo | Función |
|---|---|
| `index.html` | **Versión autónoma** (todo incrustado): funciona sola, abriéndola o en GitHub Pages |
| `src/` | Código fuente editable (`template.html`, `engine.js`, `app.js`, `fx.js`). Tras editar, ejecuta `python3 build.py` |
| `engine.js` | Motor con reglas oficiales (validado con perft: 20 · 400 · 8 902 · 197 281) |
| `app.js` | UI, guía CLI, XP, ranking, comunidad y panel admin |
| `fx.js` | Sonidos sintetizados, voz en español y efectos (sin archivos de audio) |
| `assets/` | Logos de Proyecto Sapientia (ícono y horizontal, claro y oscuro) y favicon |
| `schema.json` | Esquema de datos: partida, usuario, XP e insignia |
| `COMPONENTES.md` | Especificación de componentes React/Tailwind |

## Publicar en GitHub Pages
1. Crea un repositorio y sube todos los archivos a la raíz.
2. *Settings → Pages → Deploy from a branch → `main` / `/ (root)`*.
3. Tu sitio quedará en `https://<usuario>.github.io/<repositorio>/`.

## Qué funciona hoy
- Reglas completas: enroque, captura al paso, coronación, jaque mate, ahogado y repetición triple (jaque perpetuo).
- Modo reflexivo (2 jugadores, sin tiempo) y competitivo contra El Guía con Elo.
- Propósitos por pieza → XP, medallas, skins y títulos ("Estratega Consciente").
- Salas con enlace (`#sala=CÓDIGO`): sincronizan entre pestañas del mismo navegador (demostración).
- Muro con filtro antiacoso, ranking por Elo/XP y panel de insignias `VERIFICADO ▲`.

## Sonido, voz y animaciones
- Pantalla de entrada con el ícono de Sapientia; el botón *Entrar* activa audio y voz (los navegadores lo exigen).
- Sonidos propios para mover, capturar, enroque, coronación, jaque, XP, tablas y jaque mate.
- Voz narra jugadas, jaque, resultado, logros y frases de El Guía. Se apaga con los botones *Sonido* y *Voz*.
- Piezas que se deslizan, destello dorado al capturar, pulso en el rey en jaque y lluvia de destellos al ganar. Respeta `prefers-reduced-motion`.
- La voz depende de las voces en español instaladas en el dispositivo.

## Límites honestos de esta versión
Los datos del jugador se guardan en `localStorage`. El multijugador es P2P (PeerJS) y el ranking global es opcional (Supabase). El panel Admin de la página es una demostración local: con ranking global, la insignia se asigna desde el panel de Supabase.

## Roadmap técnico
**Fase 1 · Frontend (completada)** — tablero, reflexión, guía CLI, gamificación local.
**Fase 2 · Backend** — Supabase o Firebase: autenticación, tablas `usuarios`, `partidas`, `xp_eventos`, `publicaciones`; reglas RLS; rol `admin` real.
**Fase 3 · Realtime** — canales por sala (Supabase Realtime / WebSocket), validación de jugadas en servidor con `engine.js`, reconexión.
**Fase 4 · Matchmaking** — cola por Elo (±100, ampliable con el tiempo), cálculo de Elo en servidor, ranking global.
**Fase 5 · Moderación** — filtro de acoso en servidor, reportes, revisión manual.

## Ajustes de diseño
Tokens en `:root` de `index.html`. El tracking de `-0.06em` se aplica a títulos; el cuerpo usa `-0.02em` para conservar legibilidad.

## Multijugador entre dispositivos (P2P)
Pulsa *Crear sala*, comparte el enlace (`#sala=CÓDIGO`) y tu rival jugará con Negras. Usa WebRTC con PeerJS y su servidor de señalización público: **requiere internet y que la página se sirva por HTTPS (GitHub Pages)**. En redes muy restrictivas puede fallar sin un servidor TURN. Sin PeerJS cargado, la sala funciona entre pestañas del mismo navegador.

## App instalable (PWA)
`manifest.webmanifest`, `sw.js` e `icons/` hacen que MindChess se instale (botón *Instalar app*, o "Añadir a pantalla de inicio") y abra sin conexión. Solo funciona servido por HTTPS.

## Ranking global (opcional)
1. Crea un proyecto en supabase.com y ejecuta `supabase/schema.sql` en *SQL Editor*.
2. Copia la URL y la clave *anon public* en `config.js`.
3. Sube `config.js`. El Elo y el XP se sincronizan al terminar cada partida.
Prototipo: sin autenticación; para producción añade Supabase Auth (nota en el SQL).

## Archivos de GitHub
`index.html` · `manifest.webmanifest` · `sw.js` · `config.js` · `icons/` · `supabase/` · `README.md` (más `src/`, `assets/`, `build.py` para editar).
