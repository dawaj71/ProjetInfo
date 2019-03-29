package com.example.jb.frontend;
import android.util.Log;
import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;
import org.json.JSONException;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.HttpHeaderParser;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Map;

public class SecondActivity extends AppCompatActivity {
    Bitmap bitmap;
    final String URL = "http://192.168.43.159:8000/img_searches";
    private int imageServerId;
    private double score11, score22, score33;
    private String img641, img642, img643, score1, score2, score3;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.secondactivity);
        ImageView mImageView = (ImageView) findViewById(R.id.image);

        //  byte[] byteArray = getIntent().getByteAExtra("image");
        // Bitmap imageBitmap = BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
        bitmap = getIntent().getParcelableExtra("Bitmap");
        mImageView.setImageBitmap(bitmap);
        Button dkeep = (Button) findViewById(R.id.button2);
        Button keep = (Button) findViewById(R.id.button);


        keep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //envoyer l'image par commande POST au serveur
                ByteArrayOutputStream baos = new ByteArrayOutputStream();
                bitmap.compress(Bitmap.CompressFormat.JPEG, 100, baos);
                byte[] imageBytes = baos.toByteArray();
                final String imageString = Base64.encodeToString(imageBytes, Base64.DEFAULT);
                HashMap<String, String> parameters = new HashMap<>();
                parameters.put("img64", imageString);
                parameters.put("name", "MyImage");


                JsonObjectRequest request = new JsonObjectRequest(Request.Method.POST, URL, new JSONObject(parameters), new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject s) {
                        try {
                            if (s.getBoolean("Success")) {
                                imageServerId = s.getInt("Key");
                                getData();

                            } else {
                                Toast.makeText(SecondActivity.this, "Some error occurred!", Toast.LENGTH_LONG).show();
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError volleyError) {
                        Toast.makeText(SecondActivity.this, "Some error occurred -> " + volleyError, Toast.LENGTH_LONG).show();
                        ;
                    }
                });

                RequestQueue rQueue = Volley.newRequestQueue(SecondActivity.this);
                rQueue.add(request);
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


    private void getData() {
        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                String.format("%s/%s", URL, imageServerId),
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            if (response.getBoolean("Success")) {
                                score11 = response.getDouble("Score1");
                                score22 = response.getDouble("Score2");
                                score33 = response.getDouble("Score3");
                                img641 = response.getString("img1b64");
                                img642 = response.getString("img2b64");
                                img643 = response.getString("img3b64");

                                score1 = String.valueOf(score11);
                                score2 = String.valueOf(score22);
                                score3 = String.valueOf(score33);

                                Intent in2 = new Intent(SecondActivity.this, Thirdactivity.class);
                                in2.putExtra("Score1",score1);
                                in2.putExtra("Score2", score2);
                                in2.putExtra("Score3", score3);
                                in2.putExtra("img1", img641);
                                in2.putExtra("img2", img642);
                                in2.putExtra("img3", img643);
                                startActivity(in2);
                            }
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        error.printStackTrace();
                    }
                });
        RequestQueue requestQueue = Volley.newRequestQueue(SecondActivity.this);
        requestQueue.add(request);
    }
}
