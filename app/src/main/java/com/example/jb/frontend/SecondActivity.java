package com.example.jb.frontend;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class SecondActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.secondactivity);
        ImageView mImageView = (ImageView) findViewById(R.id.image);
      //  byte[] byteArray = getIntent().getByteAExtra("image");
       // Bitmap imageBitmap = BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
        Bitmap imageBitmap = getIntent().getParcelableExtra("Bitmap");
        mImageView.setImageBitmap(imageBitmap);

        Button dkeep = (Button) findViewById(R.id.button2);
        Button keep = (Button) findViewById(R.id.button);


        keep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //envoyer l'image par commande POST au serveur
            }
        });
        dkeep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent in2 = new Intent(SecondActivity.this, MainActivity.class);
                startActivity(in2);
            }
        });

        }

    }


