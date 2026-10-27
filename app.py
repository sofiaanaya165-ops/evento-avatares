import os
import gradio as gr

CSS = """
.gradio-container {
    max-width: 1100px !important;
    margin: auto !important;
    background: #f4f7fb !important;
    color: #172033 !important;
}
footer { display: none !important; }
"""

PAGINA = """
<div style="font-family:Arial,sans-serif;color:#172033;
padding:30px 20px;background:#f4f7fb;border-radius:22px;">

  <div style="text-align:center;background:#ffffff;
  padding:30px 20px;border-radius:22px;border:1px solid #dbe3f0;">

    <p style="color:#5b21b6;font-weight:bold;letter-spacing:2px;">
    TECNOFEST-2026
    </p>

    <div style="font-size:55px;">🤖✨</div>

    <h1 style="font-size:clamp(30px,5vw,46px);
    color:#172554;margin:15px 0;">
    ¡Crea tu avatar con inteligencia artificial!
    </h1>

    <p style="font-size:18px;line-height:1.7;color:#334155;
    max-width:650px;margin:15px auto;">
    Convierte tu fotografía en un personaje digital.
    Sigue los pasos y descubre tu creatividad con inteligencia artificial.
    </p>

    <div style="display:flex;flex-wrap:wrap;gap:14px;
    justify-content:center;margin:30px 0 10px;">

      <a href="https://www.toonizer.com/" target="_blank"
      rel="noopener noreferrer"
      style="background:#6d28d9;color:#ffffff;text-decoration:none;
      padding:17px 22px;border-radius:12px;font-weight:bold;
      font-size:16px;display:inline-block;">
      ✨ Crear mi avatar en Toonizer
      </a>

      <a href="https://www.toonizer.com/" target="_blank"
      rel="noopener noreferrer"
      style="background:#172554;color:#ffffff;text-decoration:none;
      padding:17px 22px;border-radius:12px;font-weight:bold;
      font-size:16px;display:inline-block;">
      🌐 Entrar directamente a Toonizer
      </a>
    </div>
  </div>

  <h2 style="text-align:center;color:#172554;margin:32px 0 18px;">
  ¿Cómo crear tu avatar?
  </h2>

  <div style="display:flex;flex-wrap:wrap;gap:16px;">

    <div style="flex:1;min-width:200px;background:#ffffff;
    border:1px solid #dbe3f0;border-radius:16px;padding:22px;">
      <div style="font-size:36px;">📸</div>
      <h3 style="color:#5b21b6;">1. Prepara tu foto</h3>
      <p style="color:#334155;line-height:1.8;">
      Elige una fotografía clara. Utiliza una imagen propia
      o una para la que tengas autorización.
      </p>
    </div>

    <div style="flex:1;min-width:200px;background:#ffffff;
    border:1px solid #dbe3f0;border-radius:16px;padding:22px;">
      <div style="font-size:36px;">🎨</div>
      <h3 style="color:#5b21b6;">2. Crea tu avatar</h3>
      <p style="color:#334155;line-height:1.8;">
      Entra a Toonizer, sigue las instrucciones de la plataforma
      y selecciona el estilo disponible.
      </p>
    </div>

    <div style="flex:1;min-width:200px;background:#ffffff;
    border:1px solid #dbe3f0;border-radius:16px;padding:22px;">
      <div style="font-size:36px;">📲</div>
      <h3 style="color:#5b21b6;">3. Guarda tu creación</h3>
      <p style="color:#334155;line-height:1.8;">
      Cuando termines, utiliza las opciones de Toonizer
      para guardar tu avatar.
      </p>
    </div>
  </div>

  <div style="margin-top:22px;background:#ede9fe;
  border-left:5px solid #6d28d9;border-radius:10px;padding:18px;">
    <strong style="color:#4c1d95;">🔒 Importante:</strong>
    <span style="color:#312e81;line-height:1.8;">
    Revisa las condiciones de Toonizer. El inicio de sesión y los límites
    de generación dependen de esa plataforma. No compartas contraseñas
    ni fotografías de otras personas sin permiso.
    </span>
  </div>

  <p style="text-align:center;color:#475569;margin-top:28px;">
  Proyecto educativo · Evento de tecnología
  </p>
</div>
"""
with gr.Blocks(title="TECNOFEST 2026") as app:
    gr.HTML(PAGINA)

if __name__ == "__main__":
     app.launch(
        theme=gr.themes.Soft(primary_hue="violet"),
        css=CSS,
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 10000)),
        share=False
      )
