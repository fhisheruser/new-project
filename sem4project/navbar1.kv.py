WindowManager:
    navbar1:
    about:


<navbar1>:
    # Creating AnchorLayout
    AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'center'

            # Canvas creation
            canvas:
                    Color:
                            rgb: [1, 1, 1]
                    Rectangle:
                            pos: self.pos
                            size: self.size
            
            about:
                    size_hint: [None, None]
                    size: [app.x, app.y]

    BoxLayout:
        padding: '5dp'
        adaptive_height: True
        
        about_button:
            text: 'About'
            on_release: app.root.current = "about"

<about>:
	AnchorLayout:
		anchor_x: 'center'
		anchor_y: 'center'
		canvas:
			Color:
				rgba: [1, 1, 1, 1]
			Rectangle:
				pos: self.pos
				size: self.size
		
